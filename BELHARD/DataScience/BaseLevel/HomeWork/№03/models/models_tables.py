from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, DateTime

Base = declarative_base()


class Gender(Base):
    __tablename__ = 'genders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(String)

class BloodType(Base):
    __tablename__ = 'blood_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    blood_type = Column(String)

class MedicalCondition(Base):
    __tablename__ = 'medical_conditions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    medical_condition = Column(String)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_name = Column(String)

class Hospital(Base):
    __tablename__ = 'hospitals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hospital_name = Column(String)

class InsuranceProvider(Base):
    __tablename__ = 'insurance_providers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    insurance_provider = Column(String)

class AdmissionType(Base):
    __tablename__ = 'admission_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    admission_type = Column(String)

class Medication(Base):
    __tablename__ = 'medications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    medication = Column(String)

class TestResults(Base):
    __tablename__ = 'test_results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    test_result = Column(String)


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    Age = Column(Integer)
    DateAdmission = Column(Date)
    BillingAmount = Column(Float)
    RoomNumber = Column(Integer)
    DischargeDate = Column(Date)
    LengthStay = Column(Integer)