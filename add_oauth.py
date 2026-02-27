import re

with open('app.py', 'r') as f:
    content = f.read()

# Add import if not present
if 'from oauth_routes import register_oauth_routes' not in content:
    content = content.replace(
        'from email.mime.multipart import MIMEMultipart',
        'from email.mime.multipart import MIMEMultipart\nfrom oauth_routes import register_oauth_routes'
    )
    
    # Add registration after app.secret_key
    content = content.replace(
        'app.secret_key = "scholarship_portal_secret_key_2024"',
        'app.secret_key = "scholarship_portal_secret_key_2024"\n\n# Register OAuth routes\nregister_oauth_routes(app)'
    )
    
    with open('app.py', 'w') as f:
        f.write(content)
    print('OAuth routes registered successfully!')
else:
    print('OAuth routes already registered')
