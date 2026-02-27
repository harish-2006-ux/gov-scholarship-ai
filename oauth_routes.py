# OAuth Routes for Google & DigiLocker Login
# Add these routes to your app.py

# 1. Add this import at the top of app.py:
# from oauth_routes import register_oauth_routes
# 
# 2. Add this after app initialization in app.py:
# register_oauth_routes(app)

def register_oauth_routes(app):
    """Register OAuth routes with the Flask app"""
    from flask import request, url_for, redirect, flash, session
    from models import Session, User, Visit
    from werkzeug.security import generate_password_hash
    
    # Try to import OAuth libraries
    try:
        from authlib.integrations.flask_client import OAuth
        oauth = OAuth(app)
        
        # Import config
        try:
            import config
            GOOGLE_CLIENT_ID = getattr(config, 'GOOGLE_CLIENT_ID', 'YOUR_GOOGLE_CLIENT_ID')
            GOOGLE_CLIENT_SECRET = getattr(config, 'GOOGLE_CLIENT_SECRET', 'YOUR_GOOGLE_CLIENT_SECRET')
        except:
            GOOGLE_CLIENT_ID = 'YOUR_GOOGLE_CLIENT_ID'
            GOOGLE_CLIENT_SECRET = 'YOUR_GOOGLE_CLIENT_SECRET'
        
        # Google OAuth Configuration
        google = oauth.register(
            name='google',
            client_id=GOOGLE_CLIENT_ID,
            client_secret=GOOGLE_CLIENT_SECRET,
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            client_kwargs={'scope': 'openid email profile'},
        )
        
        GOOGLE_CONFIGURED = GOOGLE_CLIENT_ID != 'YOUR_GOOGLE_CLIENT_ID'
    except Exception as e:
        print(f"OAuth configuration warning: {e}")
        google = None
        GOOGLE_CONFIGURED = False
    
    def handle_oauth_callback(user_info, provider):
        """Handle OAuth callback - login or register user"""
        db_session = Session()
        try:
            user = db_session.query(User).filter_by(email=user_info['email']).first()
            
            if user:
                session['user_id'] = user.id
                session['user_name'] = user.first_name
                session['user_email'] = user.email
            else:
                name_parts = user_info.get('name', '').split()
                new_user = User(
                    first_name=name_parts[0] if name_parts else 'User',
                    last_name=' '.join(name_parts[1:]) if len(name_parts) > 1 else '',
                    email=user_info['email'],
                    password_hash=generate_password_hash(f"oauth_{provider}_{user_info['email']}"),
                    digilocker_id=f"{provider}_{user_info.get('sub', '')}"
                )
                db_session.add(new_user)
                db_session.commit()
                session['user_id'] = new_user.id
                session['user_name'] = new_user.first_name
                session['user_email'] = new_user.email
            
            visit = Visit(user_id=session['user_id'], page="login", action=f"oauth_{provider}_login")
            db_session.add(visit)
            db_session.commit()
            return True
        except Exception as e:
            print(f"OAuth callback error: {e}")
            db_session.rollback()
            return False
        finally:
            db_session.close()

    # Google OAuth Routes
    @app.route("/auth/google")
    def auth_google():
        """Initiate Google OAuth login"""
        if not GOOGLE_CONFIGURED:
            flash("Google OAuth not configured. Please set credentials in config.py", "error")
            return redirect(url_for('signup'))
        
        redirect_uri = url_for('auth_google_callback', _external=True)
        return google.authorize_redirect(redirect_uri)

    @app.route("/auth/google/callback")
    def auth_google_callback():
        """Handle Google OAuth callback"""
        try:
            token = google.authorize_access_token()
            user_info = google.parse_id_token(token)
            
            if handle_oauth_callback(user_info, 'google'):
                flash("Successfully logged in with Google!", "success")
                return redirect(url_for('profile'))
            else:
                flash("Failed to login with Google", "error")
                return redirect(url_for('signup'))
        except Exception as e:
            flash(f"Google login failed: {str(e)}", "error")
            return redirect(url_for('signup'))

    # DigiLocker OAuth Routes
    @app.route("/auth/digilocker")
    def auth_digilocker():
        """Initiate DigiLocker OAuth login"""
        try:
            import config
            digilocker_client_id = getattr(config, 'DIGILOCKER_CLIENT_ID', 'YOUR_DIGILOCKER_CLIENT_ID')
        except:
            digilocker_client_id = 'YOUR_DIGILOCKER_CLIENT_ID'
        
        if digilocker_client_id == 'YOUR_DIGILOCKER_CLIENT_ID':
            # Demo mode - redirect to callback with demo flag
            flash("DigiLocker OAuth in demo mode", "info")
            return redirect(url_for('auth_digilocker_callback', demo='true'))
        
        redirect_uri = url_for('auth_digilocker_callback', _external=True)
        digilocker_auth_url = f"https://digitallocker.gov.in/oauth2/auth?response_type=code&client_id={digilocker_client_id}&redirect_uri={redirect_uri}&scope=profile"
        return redirect(digilocker_auth_url)

    @app.route("/auth/digilocker/callback")
    def auth_digilocker_callback():
        """Handle DigiLocker OAuth callback"""
        try:
            code = request.args.get('code')
            demo = request.args.get('demo')
            
            if not code:
                if demo:
                    # Demo mode - create test user
                    demo_user_info = {
                        'email': 'demo@digilocker.example.com',
                        'name': 'DigiLocker Demo User',
                        'sub': 'demo123'
                    }
                    if handle_oauth_callback(demo_user_info, 'digilocker'):
                        flash("Logged in with DigiLocker (Demo mode)!", "success")
                        return redirect(url_for('profile'))
                
                flash("DigiLocker authorization failed", "error")
                return redirect(url_for('signup'))
            
            # Real DigiLocker OAuth flow
            try:
                import config
                digilocker_client_id = getattr(config, 'DIGILOCKER_CLIENT_ID', 'YOUR_DIGILOCKER_CLIENT_ID')
                digilocker_client_secret = getattr(config, 'DIGILOCKER_CLIENT_SECRET', 'YOUR_DIGILOCKER_CLIENT_SECRET')
            except:
                flash("DigiLocker not configured", "error")
                return redirect(url_for('signup'))
            
            redirect_uri = url_for('auth_digilocker_callback', _external=True)
            
            import requests
            token_url = "https://digitallocker.gov.in/oauth2/token"
            token_data = {
                'grant_type': 'authorization_code',
                'code': code,
                'client_id': digilocker_client_id,
                'client_secret': digilocker_client_secret,
                'redirect_uri': redirect_uri
            }
            
            response = requests.post(token_url, data=token_data)
            
            if response.status_code == 200:
                token = response.json()
                access_token = token.get('access_token')
                
                profile_url = "https://digitallocker.gov.in/oauth2/userinfo"
                headers = {'Authorization': f'Bearer {access_token}'}
                profile_response = requests.get(profile_url, headers=headers)
                
                if profile_response.status_code == 200:
                    user_info = profile_response.json()
                    if handle_oauth_callback(user_info, 'digilocker'):
                        flash("Successfully logged in with DigiLocker!", "success")
                        return redirect(url_for('profile'))
            
            flash("DigiLocker authentication failed", "error")
            return redirect(url_for('signup'))
        except Exception as e:
            flash(f"DigiLocker login error: {str(e)}", "error")
            return redirect(url_for('signup'))
    
    print("OAuth routes registered successfully!")
    return app
