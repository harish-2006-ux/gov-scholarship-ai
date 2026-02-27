# insert_ssp_scholarships.py
# ------------------------------------------------------------
# Insert SSP (Student Scholarship Portal) Karnataka Scholarships
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

# ---------- 2️⃣  Prepare the data - SSP Scholarships ----------
scholarships = [
    # =====================================================
    # SSP (Student Scholarship Portal) Karnataka Scholarships
    # =====================================================
    
    # PRE-MATRIC SCHOLARSHIPS (Class 1-10)
    Scholarship(
        name="SSP Pre-Matric Scholarship (SC Students)",
        description="SSP Pre-matric scholarship for SC students studying in Class 1-10 in Karnataka.",
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
        name="SSP Pre-Matric Scholarship (ST Students)",
        description="SSP Pre-matric scholarship for ST students studying in Class 1-10 in Karnataka.",
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
        name="SSP Pre-Matric Scholarship (OBC Students)",
        description="SSP Pre-matric scholarship for OBC students studying in Class 1-10 in Karnataka.",
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
        name="SSP Pre-Matric Government School Scholarship",
        description="SSP scholarship for students studying in Government schools (Class 1-10).",
        min_age=5,
        max_age=15,
        max_income=250000.0,
        caste_allowed="SC,ST,OBC",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, School ID",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # POST-MATRIC SCHOLARSHIPS (PUC, Degree, etc.)
    Scholarship(
        name="SSP Post-Matric Scholarship (SC - Day Scholars)",
        description="SSP scholarship for SC students studying as day scholars in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="SC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Institution verification",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (SC - Hostellers)",
        description="SSP scholarship for SC students staying in hostels in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="SC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Hostel certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (ST - Day Scholars)",
        description="SSP scholarship for ST students studying as day scholars in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="ST",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Institution verification",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (ST - Hostellers)",
        description="SSP scholarship for ST students staying in hostels in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="ST",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Hostel certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (OBC - Day Scholars)",
        description="SSP scholarship for OBC students studying as day scholars in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="OBC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Institution verification",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (OBC - Hostellers)",
        description="SSP scholarship for OBC students staying in hostels in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="OBC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Hostel certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # SSP Vidyasiri Scholarship
    Scholarship(
        name="SSP Vidyasiri Scholarship (BCM - Karnataka)",
        description="SSP Vidyasiri scholarship for OBC, BCM, category students pursuing PUC in Karnataka.",
        min_age=16,
        max_age=25,
        max_income=250000.0,
        caste_allowed="OBC,BCM",
        gender_allowed="Any",
        course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Vidyasiri Scholarship Degree",
        description="SSP Vidyasiri scholarship for OBC, BCM students pursuing degree courses in Karnataka.",
        min_age=17,
        max_age=28,
        max_income=250000.0,
        caste_allowed="OBC,BCM",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # SSP Minority Scholarships
    Scholarship(
        name="SSP Minority Scholarship (Muslims)",
        description="SSP scholarship for Muslim minority students in Karnataka.",
        min_age=15,
        max_age=30,
        max_income=250000.0,
        caste_allowed="Muslim",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Previous year marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Minority Scholarship (Christians)",
        description="SSP scholarship for Christian minority students in Karnataka.",
        min_age=15,
        max_age=30,
        max_income=250000.0,
        caste_allowed="Christian",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Previous year marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Minority Scholarship (Sikhs)",
        description="SSP scholarship for Sikh minority students in Karnataka.",
        min_age=15,
        max_age=30,
        max_income=250000.0,
        caste_allowed="Sikh",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Previous year marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Minority Scholarship (Buddhists)",
        description="SSP scholarship for Buddhist minority students in Karnataka.",
        min_age=15,
        max_age=30,
        max_income=250000.0,
        caste_allowed="Buddhist",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Previous year marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Minority Scholarship (Jains)",
        description="SSP scholarship for Jain minority students in Karnataka.",
        min_age=15,
        max_age=30,
        max_income=250000.0,
        caste_allowed="Jain",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Previous year marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # SSP Degree Colleges
    Scholarship(
        name="SSP Degree College Scholarship (SC/ST)",
        description="SSP scholarship for SC/ST students pursuing regular degree courses in Karnataka.",
        min_age=17,
        max_age=35,
        max_income=250000.0,
        caste_allowed="SC,ST",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Bonafide certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Degree College Scholarship (OBC)",
        description="SSP scholarship for OBC students pursuing regular degree courses in Karnataka.",
        min_age=17,
        max_age=35,
        max_income=250000.0,
        caste_allowed="OBC",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous year marksheet, Bank account, Aadhaar, Bonafide certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # SSP Professional Courses
    Scholarship(
        name="SSP Professional Courses Scholarship (Medical)",
        description="SSP scholarship for students pursuing Medical (MBBS/BDS) courses in Karnataka.",
        min_age=17,
        max_age=30,
        max_income=250000.0,
        caste_allowed="SC,ST,OBC",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Professional Courses Scholarship (Engineering)",
        description="SSP scholarship for students pursuing Engineering (BE/BTech) courses in Karnataka.",
        min_age=17,
        max_age=30,
        max_income=250000.0,
        caste_allowed="SC,ST,OBC",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Professional Courses Scholarship (Law)",
        description="SSP scholarship for students pursuing Law (LLB/LLM) courses in Karnataka.",
        min_age=17,
        max_age=30,
        max_income=250000.0,
        caste_allowed="SC,ST,OBC",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # SSP Vocational Courses
    Scholarship(
        name="SSP Vocational Education Scholarship (ITI)",
        description="SSP scholarship for students pursuing ITI vocational courses in Karnataka.",
        min_age=15,
        max_age=30,
        max_income=250000.0,
        caste_allowed="SC,ST,OBC",
        gender_allowed="Any",
        course_allowed="Vocational",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Vocational Education Scholarship (Polytechnic)",
        description="SSP scholarship for students pursuing Polytechnic/Diploma courses in Karnataka.",
        min_age=15,
        max_age=30,
        max_income=250000.0,
        caste_allowed="SC,ST,OBC",
        gender_allowed="Any",
        course_allowed="Vocational",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # SSP Special Categories
    Scholarship(
        name="SSP Transgender Scholarship",
        description="SSP scholarship for transgender students in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="Any",
        gender_allowed="Other",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Identity certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Differently Abled Scholarship",
        description="SSP scholarship for differently-abled students in Karnataka.",
        min_age=15,
        max_age=35,
        max_income=250000.0,
        caste_allowed="Any",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Disability certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # SSP Fee Reimbursement
    Scholarship(
        name="SSP Fee Reimbursement Scheme (SC/ST)",
        description="Fee reimbursement for SC/ST students enrolled in professional courses in Karnataka.",
        min_age=17,
        max_age=30,
        max_income=250000.0,
        caste_allowed="SC,ST",
        gender_allowed="Any",
        course_allowed="Degree",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission fee receipt, Bank account details",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    
    # NSP Central Scholarships (via SSP)
    Scholarship(
        name="NSP Post Matric Scholarship (SC - Central)",
        description="Central scholarship for SC students pursuing post-matriculation courses via SSP portal.",
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
        description="Central scholarship for ST students pursuing post-matriculation courses via SSP portal.",
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
        name="NSP Post Matric Scholarship (OBC - Central)",
        description="Central scholarship for OBC students pursuing post-matriculation courses via SSP portal.",
        min_age=16,
        max_age=30,
        max_income=250000.0,
        caste_allowed="OBC",
        gender_allowed="Any",
        course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://scholarships.gov.in/"
    ),
    
    # PM YASASVI Scholarships
    Scholarship(
        name="PM YASASVI Pre-Matric Scholarship (OBC, EBC, DNT)",
        description="PM YASASVI pre-matric scholarship for OBC, EBC and DNT students in Karnataka.",
        min_age=8,
        max_age=18,
        max_income=250000.0,
        caste_allowed="OBC,EBC",
        gender_allowed="Any",
        course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account details",
        official_url="https://yet.nta.ac.in/"
    ),
    Scholarship(
        name="PM YASASVI Post-Matric Scholarship (OBC, EBC, DNT)",
        description="PM YASASVI post-matric scholarship for OBC, EBC and DNT students in Karnataka.",
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
    
    # AICTE Scholarships via SSP
    Scholarship(
        name="Pragati Scholarship for Girls (AICTE)",
        description="Scholarship for girl students admitted to AICTE-approved degree programmes via SSP.",
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
        description="Scholarship for divyang (disabled) students pursuing degree programmes via SSP.",
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

print(f"Successfully inserted {len(scholarships)} SSP scholarship records into the database.")
