import os

from d_base import db_cerate
from loader import load_data_csv, load_kaggle_data_set
from config import dataset_path
from datetime import date
from models.models_tables import Patient
from d_base import create_tables, add_patient, add_all_from_dataset_to_table


kaggle_data_set = 'eduardolicea/healthcare-dataset'


separator = f"\n{'-'*100}\n"

if __name__ == '__main__':
    try:
        if not os.path.exists(dataset_path):
            load_kaggle_data_set(kaggle_data_set)               # Загрузка файла датасета из kaggle если он не загружен
        df = load_data_csv(dataset_path)                        # Загрузка файла в датафрейм

        df.info()                                           # Информация о датафрейме (датасете)

        print(separator,
              'Отсутствующие значения:\n',
              df.isna().sum())                              # Отсутствующие значения в столбцах датафрейма. Можно посмотреть и в информации, но так более наглядно.

        print(separator,
              'Количество дублирующихся значений: ',
              df.duplicated().sum())

        df.rename(columns={'Blood Type'         : 'BloodType',
                           'Medical Condition'  : 'MedicalCondition',
                           'Date of Admission'  : 'DateOfAdmission',
                           'Insurance Provider' : 'InsuranceProvider',
                           'Billing Amount'     : 'BillingAmount',
                           'Room Number'        : 'RoomNumber',
                           'Admission Type'     : 'AdmissionType',
                           'Discharge Date'     : 'DischargeDate',
                           'Test Results'       : 'TestResults',
                           'Length of Stay'     : 'LengthOfStay'
                           },
                  inplace=True
        )                                                                   # Переименовать столбцы лоя дальнейшей работы
        df.info()                                                           # Информация о датафрейме (датасете)

        db_cerate()                                                         # Создать БД

        create_tables()                                                     # Создать таблицы в БД

        add_all_from_dataset_to_table(df,'genders',['Gender'])
        add_all_from_dataset_to_table(df,'blood_types',['BloodType'])
        add_all_from_dataset_to_table(df,'medical_conditions',['MedicalCondition'])
        add_all_from_dataset_to_table(df,'doctors',['Doctor'])
        add_all_from_dataset_to_table(df,'hospitals',['Hospital'])
        add_all_from_dataset_to_table(df,'insurance_providers',['InsuranceProvider'])
        add_all_from_dataset_to_table(df,'admission_types',['AdmissionType'])
        add_all_from_dataset_to_table(df,'medications',['Medication'])
        add_all_from_dataset_to_table(df,'test_results',['TestResults'])
        add_all_from_dataset_to_table(df,'patients')


        # patient = Patient(Name='Bobby Jackson',
        #                   Age=19,
        #                   DateAdmission=date.fromisoformat('2024-01-31'),
        #                   BillingAmount = 2212.272701009033,
        #                   RoomNumber = 1,
        #                   DischargeDate = date.fromisoformat('2024-02-07'),
        #                   LengthStay=7,
        #                   )

        # add_patient(patient)

    except Exception as e:
        print(f'При выполнении произошла ошибка: {e}')

