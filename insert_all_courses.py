# insert_all_courses.py
# ------------------------------------------------------------
# Insert Karnataka Scholarships for ALL Course Levels
# School, PUC, Undergraduate, Postgraduate, PhD
# ------------------------------------------------------------

from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------- Database Setup ----------
engine = create_engine("sqlite:///database.db", echo=False)
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

# ---------- Prepare Data for ALL Course Levels ----------
scholarships = [
    # =====================================================
    # SCHOOL (Class 1-10) SCHOLARSHIPS
    # =====================================================
    Scholarship(
        name="SSP Pre-Matric Scholarship (SC Students - School)",
        description="Pre-matric scholarship for SC students in Class 1-10 in Karnataka.",
        min_age=5, max_age=15, max_income=250000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Pre-Matric Scholarship (ST Students - School)",
        description="Pre-matric scholarship for ST students in Class 1-10 in Karnataka.",
        min_age=5, max_age=15, max_income=250000.0,
        caste_allowed="ST", gender_allowed="Any", course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Pre-Matric Scholarship (OBC Students - School)",
        description="Pre-matric scholarship for OBC students in Class 1-10 in Karnataka.",
        min_age=5, max_age=15, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Pre-Matric Government School Scholarship",
        description="Scholarship for students in Government schools Class 1-10.",
        min_age=5, max_age=15, max_income=250000.0,
        caste_allowed="SC,ST,OBC", gender_allowed="Any", course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, School ID",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="NSP Pre-Matric Scholarship (SC - Central)",
        description="Central pre-matric scholarship for SC students Class 1-10.",
        min_age=5, max_age=15, max_income=250000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="NSP Pre-Matric Scholarship (ST - Central)",
        description="Central pre-matric scholarship for ST students Class 1-10.",
        min_age=5, max_age=15, max_income=250000.0,
        caste_allowed="ST", gender_allowed="Any", course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="PM YASASVI Pre-Matric Scholarship (OBC, EBC, DNT)",
        description="PM YASASVI pre-matric for OBC, EBC, DNT students Class 1-10.",
        min_age=8, max_age=18, max_income=250000.0,
        caste_allowed="OBC,EBC", gender_allowed="Any", course_allowed="School",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://yet.nta.ac.in/"
    ),

    # =====================================================
    # PUC (Pre-University College) SCHOLARSHIPS
    # =====================================================
    Scholarship(
        name="SSP Post-Matric Scholarship (SC - PUC)",
        description="Post-matric scholarship for SC students in PUC in Karnataka.",
        min_age=15, max_age=22, max_income=250000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (ST - PUC)",
        description="Post-matric scholarship for ST students in PUC in Karnataka.",
        min_age=15, max_age=22, max_income=250000.0,
        caste_allowed="ST", gender_allowed="Any", course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (OBC - PUC)",
        description="Post-matric scholarship for OBC students in PUC in Karnataka.",
        min_age=15, max_age=22, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Vidyasiri Scholarship (PUC)",
        description="Vidyasiri scholarship for BCM, OBC, SC, ST students in PUC.",
        min_age=15, max_age=22, max_income=250000.0,
        caste_allowed="OBC,BCM,SC,ST", gender_allowed="Any", course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="NSP Post-Matric Scholarship (SC - PUC)",
        description="National scholarship for SC students in PUC.",
        min_age=15, max_age=22, max_income=300000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="PM YASASVI Post-Matric Scholarship (PUC)",
        description="PM YASASVI scholarship for OBC, EBC, DNT students in PUC.",
        min_age=15, max_age=22, max_income=250000.0,
        caste_allowed="OBC,EBC", gender_allowed="Any", course_allowed="PUC",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://yet.nta.ac.in/"
    ),

    # =====================================================
    # UNDERGRADUATE SCHOLARSHIPS
    # =====================================================
    Scholarship(
        name="SSP Post-Matric Scholarship (SC - Undergraduate)",
        description="Post-matric scholarship for SC students pursuing Undergraduate courses.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar, Bonafide certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (ST - Undergraduate)",
        description="Post-matric scholarship for ST students pursuing Undergraduate courses.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="ST", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar, Bonafide certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (OBC - Undergraduate)",
        description="Post-matric scholarship for OBC students pursuing Undergraduate courses.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar, Bonafide certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Degree College Scholarship (SC/ST)",
        description="Scholarship for SC/ST students in regular Undergraduate degree courses.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="SC,ST", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar, Bonafide certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Degree College Scholarship (OBC)",
        description="Scholarship for OBC students in regular Undergraduate degree courses.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar, Bonafide certificate",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Vidyasiri Scholarship (Degree/Undergraduate)",
        description="Vidyasiri scholarship for OBC, BCM students in Undergraduate courses.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="OBC,BCM", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="NSP Post-Matric Scholarship (SC - Undergraduate)",
        description="National scholarship for SC students in Undergraduate courses.",
        min_age=17, max_age=28, max_income=300000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="NSP Post-Matric Scholarship (ST - Undergraduate)",
        description="National scholarship for ST students in Undergraduate courses.",
        min_age=17, max_age=28, max_income=300000.0,
        caste_allowed="ST", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="NSP Post-Matric Scholarship (OBC - Undergraduate)",
        description="National scholarship for OBC students in Undergraduate courses.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="PM YASASVI Post-Matric Scholarship (Undergraduate)",
        description="PM YASASVI scholarship for OBC, EBC, DNT students in Undergraduate.",
        min_age=17, max_age=28, max_income=250000.0,
        caste_allowed="OBC,EBC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Previous marksheet, Bank account",
        official_url="https://yet.nta.ac.in/"
    ),
    Scholarship(
        name="Pragati Scholarship for Girls (AICTE - Undergraduate)",
        description="Scholarship for girl students in AICTE-approved Undergraduate programs.",
        min_age=17, max_age=30, max_income=800000.0,
        caste_allowed="Any", gender_allowed="Female", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Admission letter, Previous marksheet, Bank account, Aadhaar",
        official_url="https://www.aicte-india.org/"
    ),
    Scholarship(
        name="Saksham Scholarship (Divyang - Undergraduate)",
        description="Scholarship for divyang students in Undergraduate courses.",
        min_age=17, max_age=30, max_income=800000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Disability certificate, Income certificate, Admission letter, Bank account",
        official_url="https://www.aicte-india.org/schemes/students-development-schemes/Saksham"
    ),
    Scholarship(
        name="Merit Cum Means Scholarship (Minority - Undergraduate)",
        description="Merit-cum-means scholarship for minority students in Undergraduate.",
        min_age=17, max_age=30, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Merit marksheet, Bank account",
        official_url="https://scholarships.gov.in/"
    ),

    # =====================================================
    # POSTGRADUATE SCHOLARSHIPS
    # =====================================================
    Scholarship(
        name="SSP Post-Matric Scholarship (SC - Postgraduate)",
        description="Post-matric scholarship for SC students in Postgraduate courses.",
        min_age=20, max_age=35, max_income=250000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Degree marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (ST - Postgraduate)",
        description="Post-matric scholarship for ST students in Postgraduate courses.",
        min_age=20, max_age=35, max_income=250000.0,
        caste_allowed="ST", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Degree marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Post-Matric Scholarship (OBC - Postgraduate)",
        description="Post-matric scholarship for OBC students in Postgraduate courses.",
        min_age=20, max_age=35, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Degree marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="NSP Post-Matric Scholarship (SC - Postgraduate)",
        description="National scholarship for SC students in Postgraduate courses.",
        min_age=20, max_age=35, max_income=300000.0,
        caste_allowed="SC", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Degree marksheet, Bank account, Aadhaar",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="NSP Post-Matric Scholarship (ST - Postgraduate)",
        description="National scholarship for ST students in Postgraduate courses.",
        min_age=20, max_age=35, max_income=300000.0,
        caste_allowed="ST", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Degree marksheet, Bank account, Aadhaar",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="NSP Post-Matric Scholarship (OBC - Postgraduate)",
        description="National scholarship for OBC students in Postgraduate courses.",
        min_age=20, max_age=35, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Degree marksheet, Bank account",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="Prime Minister's Scholarship Scheme (Postgraduate)",
        description="PM scholarship for RPF/RASF personnel wards for Postgraduate studies.",
        min_age=18, max_age=35, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="Parent's service certificate, Income certificate, Previous marksheet, Bank account",
        official_url="https://scholarships.gov.in/"
    ),
    Scholarship(
        name="AICTE PG Scholarship (GATE/GPAT)",
        description="Scholarship for GATE/GPAT qualified students in Postgraduate engineering.",
        min_age=20, max_age=35, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="Postgraduate",
        district_allowed="All",
        required_documents="GATE/GPAT scorecard, Income certificate, Degree certificate, Bank account",
        official_url="https://www.aicte-india.org/"
    ),

    # =====================================================
    # PhD SCHOLARSHIPS
    # =====================================================
    Scholarship(
        name="UGC NET JRF Scholarship (PhD)",
        description="UGC NET Junior Research Fellowship for PhD students.",
        min_age=21, max_age=40, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="PhD",
        district_allowed="All",
        required_documents="UGC NET JRF certificate, Admission letter, Income certificate, Bank account",
        official_url="https://www.ugc.ac.in/"
    ),
    Scholarship(
        name="CSIR NET JRF Scholarship (PhD)",
        description="CSIR NET Junior Research Fellowship for PhD in Science.",
        min_age=21, max_age=40, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="PhD",
        district_allowed="All",
        required_documents="CSIR NET JRF certificate, Admission letter, Income certificate, Bank account",
        official_url="https://csirnet.nta.nic.in/"
    ),
    Scholarship(
        name="INSPIRE Fellowship (PhD)",
        description="INSPIRE fellowship for PhD in Basic Sciences.",
        min_age=21, max_age=40, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="PhD",
        district_allowed="All",
        required_documents="INSPIRE fellowship offer, Income certificate, Bank account",
        official_url="https://www.inspire-dst.gov.in/"
    ),
    Scholarship(
        name="Rajiv Gandhi National Fellowship (PhD - SC/ST)",
        description="RGNF for SC/ST students pursuing PhD.",
        min_age=21, max_age=40, max_income=250000.0,
        caste_allowed="SC,ST", gender_allowed="Any", course_allowed="PhD",
        district_allowed="All",
        required_documents="Caste certificate, Admission letter, Research proposal, Bank account",
        official_url="https://socialjustice.nic.in/"
    ),
    Scholarship(
        name="National Fellowship for OBC (PhD)",
        description="National Fellowship for OBC students in PhD.",
        min_age=21, max_age=40, max_income=250000.0,
        caste_allowed="OBC", gender_allowed="Any", course_allowed="PhD",
        district_allowed="All",
        required_documents="Caste certificate, Admission letter, Research proposal, Bank account",
        official_url="https://socialjustice.nic.in/"
    ),
    Scholarship(
        name="Fellowship for Minority Students (PhD)",
        description="Fellowship for minority community students in PhD.",
        min_age=21, max_age=40, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="PhD",
        district_allowed="All",
        required_documents="Minority certificate, Admission letter, Research proposal, Bank account",
        official_url="https://minorityaffairs.gov.in/"
    ),
    Scholarship(
        name="Karnataka State Fellowship (PhD)",
        description="Karnataka State Fellowship for research scholars in state universities.",
        min_age=21, max_age=40, max_income=300000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="PhD",
        district_allowed="All",
        required_documents="Admission letter, Research proposal, No Objection Certificate, Bank account",
        official_url="https://karnataka.gov.in/"
    ),
    Scholarship(
        name="Women Scientist Fellowship (PhD)",
        description="Fellowship for women scientists in PhD research.",
        min_age=21, max_age=45, max_income=350000.0,
        caste_allowed="Any", gender_allowed="Female", course_allowed="PhD",
        district_allowed="All",
        required_documents="Research proposal, Admission letter, Bank account, Aadhaar",
        official_url="https://dst.gov.in/"
    ),

    # =====================================================
    # PROFESSIONAL COURSES (Medical, Engineering, Law)
    # =====================================================
    Scholarship(
        name="SSP Professional Courses Scholarship (Medical)",
        description="Scholarship for MBBS/BDS students in Karnataka.",
        min_age=17, max_age=30, max_income=250000.0,
        caste_allowed="SC,ST,OBC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Professional Courses Scholarship (Engineering)",
        description="Scholarship for BE/BTech students in Karnataka.",
        min_age=17, max_age=30, max_income=250000.0,
        caste_allowed="SC,ST,OBC", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Professional Courses Scholarship (Law)",
        description="Scholarship for LLB/LLM students in Karnataka.",
        min_age=17, max_age=35, max_income=250000.0,
        caste_allowed="SC,ST,OBC", gender_allowed="Any", course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Bank account",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Fee Reimbursement Scheme (Professional Courses)",
        description="Fee reimbursement for SC/ST students in professional courses.",
        min_age=17, max_age=30, max_income=250000.0,
        caste_allowed="SC,ST", gender_allowed="Any", course_allowed="Undergraduate",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission fee receipt, Bank account",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),

    # =====================================================
    # VOCATIONAL COURSES (ITI, Polytechnic)
    # =====================================================
    Scholarship(
        name="SSP Vocational Education Scholarship (ITI)",
        description="Scholarship for ITI vocational course students.",
        min_age=15, max_age=30, max_income=250000.0,
        caste_allowed="SC,ST,OBC", gender_allowed="Any", course_allowed="Vocational",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Vocational Education Scholarship (Polytechnic)",
        description="Scholarship for Polytechnic/Diploma students.",
        min_age=15, max_age=30, max_income=250000.0,
        caste_allowed="SC,ST,OBC", gender_allowed="Any", course_allowed="Vocational",
        district_allowed="All",
        required_documents="Income certificate, Caste certificate, Admission letter, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="Skill Scholarship Scheme (Vocational)",
        description="Scholarship for skill development vocational courses.",
        min_age=15, max_age=35, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="Vocational",
        district_allowed="All",
        required_documents="Income certificate, Course completion certificate, Bank account",
        official_url="https://skilldevelopment.gov.in/"
    ),

    # =====================================================
    # SPECIAL CATEGORY SCHOLARSHIPS
    # =====================================================
    Scholarship(
        name="SSP Minority Scholarship (All Religions)",
        description="Scholarship for minority community students (Muslims, Christians, Sikhs, Buddhists, Jains).",
        min_age=15, max_age=30, max_income=250000.0,
        caste_allowed="Muslim,Christian,Sikh,Buddhist,Jain", gender_allowed="Any", course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Minority certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Transgender Scholarship",
        description="Scholarship for transgender students in Karnataka.",
        min_age=15, max_age=35, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Other", course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Identity certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="SSP Differently Abled Scholarship",
        description="Scholarship for differently-abled students in Karnataka.",
        min_age=15, max_age=35, max_income=250000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="Both",
        district_allowed="All",
        required_documents="Income certificate, Disability certificate, Previous marksheet, Bank account, Aadhaar",
        official_url="https://ssp.postmatric.karnataka.gov.in/"
    ),
    Scholarship(
        name="Karnataka Labour Welfare Scholarship",
        description="Scholarship for wards of registered labour in Karnataka.",
        min_age=15, max_age=25, max_income=300000.0,
        caste_allowed="Any", gender_allowed="Any", course_allowed="Both",
        district_allowed="All",
        required_documents="Labour card, Income certificate, Previous marksheet, Bank account",
        official_url="https://klwbapps.karnataka.gov.in/"
    ),
]

# ---------- Persist to DB ----------
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing scholarships first
session.query(Scholarship).delete()
session.commit()

session.add_all(scholarships)
session.commit()
session.close()

print(f"✅ Successfully inserted {len(scholarships)} scholarships into the database!")
print("\n📚 Course Levels Covered:")
print("  - School (Class 1-10)")
print("  - PUC (Pre-University College)")
print("  - Undergraduate (Degree)")
print("  - Postgraduate (Masters)")
print("  - PhD (Doctorate)")
print("  - Vocational (ITI, Polytechnic)")
print("  - Professional (Medical, Engineering, Law)")
