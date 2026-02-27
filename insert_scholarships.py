# insert_scholarships.py
# ------------------------------------------------------------
# Insert Pre-Matric and Post-Matric Karnataka Scholarships
# ------------------------------------------------------------

from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------- 1️⃣  Database & ORM setup ----------
engine = create_engine("sqlite:///database.db", echo=True)
Base = declarative_base()

class Scholarship(Base):
    __tablename__ = "scholarships"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    min_age = Column(Integer)
    max_age = Column(Integer)
    max_income = Column(Float)
    caste_allowed = Column(String(100))
    gender_allowed = Column(String(50))
    course_allowed = Column(String(50))
    district_allowed = Column(String(100))
    required_documents = Column(Text)
    official_url = Column(String(500))

# Create the table(s)
Base.metadata.create_all(engine)

# ---------- 2️⃣  Prepare the data ----------
scholarships = [
    # PRE-MATRIC SCHOLARSHIPS (Class 1-10)
    Scholarship(
        name="Karnataka Pre-Matric Scholarship (SC Students)",
        description="Pre-matric scholarship for SC students studying in Class 1-10 in Karnataka.",
        min_age=5,
        max_age=15,
        max_income=250000.0,
        caste_allowed="SC",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="Karnataka Pre-Matric Scholarship (ST Students)",
        description="Pre-matric scholarship for ST students studying in Class 1-10 in Karnataka.",
        min_age=5,
        max_age=15,
        max_income=250000.0,
        caste_allowed="ST",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="Karnataka Pre-Matric Scholarship (OBC Students)",
        description="Pre-matric scholarship for OBC students studying in Class 1-10 in Karnataka.",
        min_age=5,
        max_age=15,
        max_income=250000.0,
        caste_allowed="OBC",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="NSP Pre-Matric Scholarship (SC - Central)",
        description="Central pre-matric scholarship for SC students in Class 1-10.",
        min_age=5,
        max_age=15,
        max_income=250000.0,
        caste_allowed="SC",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="NSP Pre-Matric Scholarship (ST - Central)",
        description="Central pre-matric scholarship for ST students in Class 1-10.",
        min_age=5,
        max_age=15,
        max_income=250000.0,
        caste_allowed="ST",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://scholarships.gov.in/"
    ),
    
    # POST-MATRIC SCHOLARSHIPS (PUC, Degree, etc.)
    Scholarship(
        name="Vidyasiri Scholarship (BCM - Karnataka)",
        description="Scholarship for OBC, SC, ST students pursuing PUC in Karnataka.",
        min_age=16,
        max_age=25,
        max_income=250000.0,
        caste_allowed="OBC,SC,ST",
        gender_allowed="Any",
        course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="Fee Reimbursement Scheme (SC/ST - Karnataka)",
        description="Fee reimbursement for SC/ST students enrolled in degree courses in Karnataka.",
        min_age=16,
        max_age=30,
        max_income=250000.0,
        caste_allowed="SC,ST",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission fee receipt, Bank account details",
        official_url="https://karnataka.gov.in/feereimbursement"
    ),
    Scholarship(
        name="Minority Scholarship (Karnataka State)",
        description="Scholarship for minority community students in Karnataka (PUC/Degree).",
        min_age=16,
        max_age=28,
        max_income=250000.0,
        caste_allowed="Any",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Previous marksheet, Bank account details",
        official_url="https://karnataka.gov.in/minority"
    ),
    Scholarship(
        name="NSP Post Matric Scholarship (SC - Central)",
        description="Central scholarship for SC students pursuing post-matriculation courses.",
        min_age=16,
        max_age=30,
        max_income=300000.0,
        caste_allowed="SC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details, Aadhaar",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="NSP Post Matric Scholarship (ST - Central)",
        description="Central scholarship for ST students pursuing post-matriculation courses.",
        min_age=16,
        max_age=30,
        max_income=300000.0,
        caste_allowed="ST",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details, Aadhaar",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="OBC Post Matric Scholarship (Central)",
        description="Central scholarship for OBC students pursuing post-matriculation courses.",
        min_age=16,
        max_age=30,
        max_income=250000.0,
        caste_allowed="OBC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://scholarships.gov.in/obc"
    ),
Scholarship(
        name="Merit Cum Means Scholarship (Minority - Central)",
        description="Merit-cum-means scholarship for minority students pursuing degree programmes.",
        min_age=17,
        max_age=30,
        max_income=250000.0,
        caste_allowed="Any",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Merit marksheet, Bank account details",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="Karnataka Labour Welfare Scholarship",
        description="Scholarship for wards of registered labour in Karnataka.",
        min_age=16,
        max_age=25,
        max_income=300000.0,
        caste_allowed="Any",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Labour card, Income certificate, Previous marksheet, Bank account details",
        official_url="https://klwbapps.karnataka.gov.in/"
    ),
    Scholarship(
        name="Pragati Scholarship for Girls (AICTE)",
        description="Scholarship for girl students admitted to AICTE-approved degree programmes.",
        min_age=17,
        max_age=30,
        max_income=800000.0,
        caste_allowed="Any",
        gender_allowed="Female",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Admission letter, Previous marksheet, Bank account details, Aadhaar",
        official_url="https://www.aicte-india.org/"
    ),
    Scholarship(
        name="Saksham Scholarship (Divyang Students - AICTE)",
        description="Scholarship for divyang (disabled) students pursuing degree programmes.",
        min_age=17,
        max_age=30,
        max_income=800000.0,
        caste_allowed="Any",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Disability certificate, Income certificate, Admission letter, Bank account details",
        official_url="https://www.aicte-india.org/schemes/students-development-schemes/Saksham"
    ),
    Scholarship(
        name="PM YASASVI Pre-Matric Scholarship (OBC, EBC, DNT)",
        description="Pre-matric scholarship for OBC, EBC and DNT students in Karnataka.",
        min_age=8,
        max_age=18,
        max_income=250000.0,
        caste_allowed="OBC,EBC",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://karnataka.gov.in/yasasi"
    ),
Scholarship(
        name="PM YASASVI Post-Matric Scholarship (OBC, EBC, DNT)",
        description="Post-matric scholarship for OBC, EBC and DNT students in Karnataka.",
        min_age=16,
        max_age=30,
        max_income=250000.0,
        caste_allowed="OBC,EBC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://yet.nta.ac.in/"
    ),
]

# ---------- 3️⃣  Persist to DB ----------
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing scholarships first
session.query(Scholarship).delete()
session.commit()

session.add_all(scholarships)
session.commit()
session.close()

print(f"Successfully inserted {len(scholarships)} scholarship records into the database.")
