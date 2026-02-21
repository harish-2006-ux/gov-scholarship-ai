from models import Session, Scholarship

session = Session()

sample1 = Scholarship(
    name="Vidyasiri Scholarship",
    description="Scholarship for OBC students in Karnataka",
    min_age=16,
    max_age=25,
    max_income=250000,
    caste_allowed="OBC",
    gender_allowed="Any",
    course_allowed="PUC",
    district_allowed="Any",
    required_documents="Income Certificate, Caste Certificate",
    official_url="https://example.com"
)

sample2 = Scholarship(
    name="SC/ST Post Matric Scholarship",
    description="Scholarship for SC/ST students",
    min_age=16,
    max_age=30,
    max_income=300000,
    caste_allowed="SC,ST",
    gender_allowed="Any",
    course_allowed="Degree",
    district_allowed="Any",
    required_documents="Caste Certificate, Aadhaar",
    official_url="https://example2.com"
)

session.add(sample1)
session.add(sample2)
session.commit()

print("Sample data inserted successfully!")