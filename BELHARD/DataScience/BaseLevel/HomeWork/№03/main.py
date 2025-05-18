import os

from d_base import db_cerate
from loader import load_data_csv, load_kaggle_data_set
from config import dataset_path
from d_base import fill_db_tabes, create_view

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
        db_cerate()                                                         # Создать БД, со всеми таблицами (таблицы пустые)
        fill_db_tabes(df)                                                   # Заполнить таблицы в БД соответствующими данными из датасета (датафрейма)


    except Exception as e:
        print(f'При выполнении произошла ошибка: {e}')

