from  d_base import Session
from models.models_tables import Patient, Base

def create_patient(patient : Patient):
    with Session() as session:
        try:
            session.add(patient)
            session.commit()
        except Exception as e:
            raise (e)
