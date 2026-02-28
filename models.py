from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

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

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    password_hash = Column(String(255), nullable=False)
    
    # Profile fields
    date_of_birth = Column(DateTime)
    gender = Column(String(20))
    caste = Column(String(50))
    district = Column(String(100))
    income = Column(Float, default=0)
    course = Column(String(50))  # School, PUC, Degree

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    applications = relationship("Application", back_populates="user")
    visits = relationship("Visit", back_populates="user")

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    scholarship_id = Column(Integer, ForeignKey("scholarships.id"))
    status = Column(String(50), default="Applied")  # Applied, Awaited, Approved, Rejected
    application_date = Column(DateTime, default=datetime.utcnow)
    documents_verified = Column(Boolean, default=False)
    notes = Column(Text)
    
    # Relationships
    user = relationship("User", back_populates="applications")
    scholarship = relationship("Scholarship")

class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    visit_date = Column(DateTime, default=datetime.utcnow)
    page = Column(String(100))
    action = Column(String(100))
    
    # Relationships
    user = relationship("User", back_populates="visits")

class UploadedDocument(Base):
    __tablename__ = "uploaded_documents"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=True)
    document_type = Column(String(100))  # income_certificate, caste_certificate, etc.
    file_name = Column(String(255))
    file_path = Column(String(500))
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    verified = Column(Boolean, default=False)
    
    # Relationships
    user = relationship("User")

class DeadlineAlert(Base):
    __tablename__ = "deadline_alerts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    scholarship_id = Column(Integer, ForeignKey("scholarships.id"))
    alert_date = Column(DateTime, default=datetime.utcnow)
    days_before = Column(Integer, default=7)  # Alert 7 days before deadline
    notified = Column(Boolean, default=False)
    
    # Relationships
    user = relationship("User")
    scholarship = relationship("Scholarship")

Session = sessionmaker(bind=engine)
