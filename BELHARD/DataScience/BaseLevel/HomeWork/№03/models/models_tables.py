from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

Base = declarative_base()


class Gender(Base):
    __tablename__ = 'genders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Gender = Column(String)

class BloodType(Base):
    __tablename__ = 'blood_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    BloodType = Column(String)

class MedicalCondition(Base):
    __tablename__ = 'medical_conditions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    MedicalCondition = Column(String)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Doctor = Column(String, unique=True)

class Hospital(Base):
    __tablename__ = 'hospitals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Hospital = Column(String)

class InsuranceProvider(Base):
    __tablename__ = 'insurance_providers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    InsuranceProvider = Column(String)

class AdmissionType(Base):
    __tablename__ = 'admission_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    AdmissionType = Column(String)

class Medication(Base):
    __tablename__ = 'medications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Medication = Column(String)

class TestResults(Base):
    __tablename__ = 'test_results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TestResults = Column(String)


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Age = Column(Integer)
    DateOfAdmission = Column(Date)
    BillingAmount = Column(Float)
    RoomNumber = Column(Integer)
    DischargeDate = Column(Date)
    LengthOfStay = Column(Integer)
