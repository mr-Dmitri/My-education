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

def add_patient(patient : Patient):
    print(patient)
    with Session() as session:
        try:
            session.add(patient)
            session.commit()
        except Exception as e:
            raise (e)

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

# Создам представление
def create_view():
    drop_view = """DROP VIEW IF EXISTS view_pat"""
    create_view = """CREATE VIEW IF NOT EXISTS view_pat AS
                     SELECT id,
                            Name
                     FROM patients
                     WHERE Age <= 15;
    """

    with engine.connect() as connection:
        try:
            connection.execute(text(drop_view))
            connection.execute(text(create_view))
        except Exception as e:
            print(f'Ошибка создания представления: {e}')

# Вызов функции для создания представления
create_view()

