import os
import json

from config import db_url
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()                                   # Базовый класс для моделей

engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)



def db_cerate():
    try:
        with Session()  as session:
            Base.metadata.create_all(engine)                # Создать базу данных (если она еще не существует)
            session.commit()
    except Exception as e:
        raise (f'Ошибка создания базы данных: {e}')


# def import_from_json(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data
#
# def import_rates_from_json_file(file_path):
#     data = import_from_json(file_path)
#
#     engine = create_engine(database_url)
#     with Session(engine) as session:
#         for row in data:
#             r = Rate(Cur_Abbreviation = row.get('Cur_Abbreviation'),
#                      Cur_ID	 = row.get('Cur_ID'),
#                      Cur_Name = row.get('Cur_Name'),
#                      Cur_OfficialRate = row.get('Cur_OfficialRate'),
#                      Cur_Scale = row.get('Cur_Scale'),
#                      Date = row.get('Date'))
#             session.add(r)
#         try:
#             session.commit()
#         except:
#             pass
#
#
# def import_rates_from_json_files(files_list):
#     for file_name in files_list:
#         import_rates_from_json_file(file_name)
#
#
# def import_currencs_from_json(file_path):
#     data = import_from_json(file_path)
#
#     base_name = 'Exrates.db'
#     base_path = os.path.abspath(os.path.dirname(__file__))
#     ful_base_name = f'{base_path}/{base_name}'
#     database_url = f'sqlite:///{ful_base_name}'
#
#     engine = create_engine(database_url)
#     with Session(engine) as session:
#         for row in data:
#             c = Currency(Cur_ID = row.get('Cur_ID'),
#                          Cur_ParentID = row.get('Cur_ParentID'),
#                          Cur_Code = row.get('Cur_Code'),
#                          Cur_Abbreviation = row.get('Cur_Abbreviation'),
#                          Cur_Name = row.get('Cur_Name'),
#                          Cur_Name_Bel = row.get('Cur_Name_Bel'),
#                          Cur_Name_Eng = row.get('Cur_Name_Eng'),
#                          Cur_QuotName = row.get('Cur_QuotName'),
#                          Cur_QuotName_Bel = row.get('Cur_QuotName_Bel'),
#                          Cur_QuotName_Eng = row.get('Cur_QuotName_Eng'),
#                          Cur_NameMulti = row.get('Cur_NameMulti'),
#                          Cur_Name_BelMulti = row.get('Cur_Name_BelMulti'),
#                          Cur_Name_EngMulti = row.get('Cur_Name_EngMulti'),
#                          Cur_Scale = row.get('Cur_Scale'),
#                          Cur_Periodicity = row.get('Cur_Periodicity'),
#                          Cur_DateStart = row.get('Cur_PeriodiCur_DateStartcity'),
#                          Cur_DateEnd = row.get('Cur_DateEnd'),
#                         )
#             try:
#                 session.add(c)
#             except:
#                 pass
#
#         session.commit()
#

