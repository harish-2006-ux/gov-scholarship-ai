from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.db", echo=True)
Base = declarative_base()

class Scholarship(Base):
    __tablename__ = "scholarships"

    id = Column(Integer, primary_key=True)
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

Session = sessionmaker(bind=engine)