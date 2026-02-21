from flask import Flask, request, jsonify, render_template
from models import Session, Scholarship

app = Flask(__name__)

# -------------------------------
# Eligibility Logic
# -------------------------------
def check_eligibility(user, scholarship):

    # --- Mandatory Checks ---

    # Age
    if not (scholarship.min_age <= user["age"] <= scholarship.max_age):
        return None

    # Income
    if user["income"] > scholarship.max_income:
        return None

    # Course
    if scholarship.course_allowed != "Both" and user["course"] != scholarship.course_allowed:
        return None

    # Caste
    if scholarship.caste_allowed != "Any":
        allowed_castes = [c.strip() for c in scholarship.caste_allowed.split(",")]
        if user["caste"] not in allowed_castes:
            return None
    
    # District
    if scholarship.district_allowed != "All":
        allowed_districts = [d.strip() for d in scholarship.district_allowed.split(",")]
        if user["district"] not in allowed_districts:
            return None

    # --- Optional Scoring ---
    score = 4  # base score because all mandatory passed

    # Gender bonus
    if scholarship.gender_allowed == "Any" or user["gender"] == scholarship.gender_allowed:
        score += 1

    return score


# -------------------------------
# Routes
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    user = request.json

    session = Session()
    scholarships = session.query(Scholarship).all()

    results = []

    for scheme in scholarships:
        score = check_eligibility(user, scheme)

        if score is not None:
            results.append({
                "name": scheme.name,
                "score": score,
                "description": scheme.description,
                "documents": scheme.required_documents,
                "url": scheme.official_url
            })

    # Sort by highest score
    results.sort(key=lambda x: x["score"], reverse=True)

    return jsonify(results)


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run()