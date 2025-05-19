import pandas as pd

from config import db_url
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from models.models_tables import Patient, Base


engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)



def db_cerate():
    try:
        with Session()  as session:
            Base.metadata.create_all(engine)                # Создать базу данных (если она еще не существует)
            session.commit()
    except Exception as e:
        raise (f'Ошибка создания базы данных: {e}')


def add_all_from_dataset_to_table(df: pd.DataFrame,
                                  table_name : str,
                                  unique_columns : list = None):
    with Session() as session:
        truncate_table = text(f'DELETE FROM {table_name}')
        session.execute(truncate_table)
        session.commit()

    inspector = inspect(engine)

    columns = [col['name'] for col in inspector.get_columns(table_name)
               if col['name']  != 'id']                                                     # Получить список столбцов из таблицы 'patients', исключая id, т.к. он автоинкриментный в таблице
    if unique_columns:                                                                      # Если передан лист имен столбцов в которых значения д.б. уникальными
        df_filtered = df[columns].drop_duplicates(unique_columns)                           # Фильтр DataFrame, оставляя только те столбцы, которые есть в таблице, и дополнительный фильтр по уникальным
    else:
        df_filtered = df[columns]                                                           # Фильтр DataFrame, оставляя только те столбцы, которые есть в таблице

    df_filtered.to_sql(table_name, con=engine, if_exists='append', index=False)             # Запись DataFrame в таблицу


def fill_db_tabes(df: pd.DataFrame):
    add_all_from_dataset_to_table(df, 'genders', ['Gender'])
    add_all_from_dataset_to_table(df, 'blood_types', ['BloodType'])
    add_all_from_dataset_to_table(df, 'medical_conditions', ['MedicalCondition'])
    add_all_from_dataset_to_table(df, 'doctors', ['Doctor'])
    add_all_from_dataset_to_table(df, 'hospitals', ['Hospital'])
    add_all_from_dataset_to_table(df, 'insurance_providers', ['InsuranceProvider'])
    add_all_from_dataset_to_table(df, 'admission_types', ['AdmissionType'])
    add_all_from_dataset_to_table(df, 'medications', ['Medication'])
    add_all_from_dataset_to_table(df, 'test_results', ['TestResults'])
    add_all_from_dataset_to_table(df, 'patients')
    add_all_from_dataset_to_table(df, 'dataset')

# Создам представление
def create_view():
    drop_view = """DROP VIEW IF EXISTS vw_patients"""
    create_view = """CREATE VIEW vw_patients AS
                     SELECT dataset.id,
                            dataset.Name,
                            dataset.Age,
                            genders.id AS GenderID,
                            blood_types.id AS BloodTypeID,
                            medical_conditions.id AS MedicalConditionID,
                            dataset.DateOfAdmission,
                            doctors.id AS DoctorID,
                            hospitals.id AS HospitalID,
                            insurance_providers.id AS InsuranceProviderID,
                            dataset.BillingAmount,
                            dataset.RoomNumber,
                            admission_types.id AS AdmissionTypeID,
                            dataset.DischargeDate,
                            medications.id AS MedicationID,
                            test_results.id,
                            dataset.LengthOfStay
                     FROM dataset
                     JOIN genders ON genders.Gender = dataset.Gender
                     JOIN blood_types ON blood_types.BloodType = dataset.BloodType
                     JOIN medical_conditions ON medical_conditions.MedicalCondition = dataset.MedicalCondition
                     JOIN doctors ON doctors.Doctor = dataset.Doctor
                     JOIN hospitals ON hospitals.Hospital = dataset.Hospital
                     JOIN insurance_providers ON insurance_providers.InsuranceProvider = dataset.InsuranceProvider
                     JOIN admission_types ON admission_types.AdmissionType = dataset.AdmissionType
                     JOIN medications ON medications.Medication = dataset.Medication
                     JOIN test_results ON test_results.TestResults = dataset.TestResults;
    """

    with engine.connect() as connection:
        try:
            connection.execute(text(drop_view))
            connection.execute(text(create_view))
        except Exception as e:
            raise (f'Ошибка создания представления: {e}')

# Вызов функции для создания представления
create_view()

