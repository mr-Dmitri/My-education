import os
from loader import load_data_csv, load_kaggle_data_set
from data_vizualizations import (sex_death_visualization, age_death_visualization,
                                 correlation_visualization, death_visualization,
                                 medical_unit_visualization)

data_path = os.path.join(os.getcwd(), 'data')
dataset = os.path.join(data_path, 'Covid Data.csv')
kaggle_data_set = 'meirnizri/covid19-dataset'

separator = f"\n{'-'*100}\n"

if __name__ == '__main__':
    try:
        if not os.path.exists(dataset):
            load_kaggle_data_set(kaggle_data_set)           # Загрузка файла датасета из kaggle если он не загружен
        df = load_data_csv(dataset)                         # Загрузка файла в датафрейм

        df.info()                                           # Информация о датафрейме (датасете)

        print(separator,
              'Отсутствующие значения:\n',
              df.isna().sum())                              # Отсутствующие значения в столбцах датафрейма. Можно посмотреть и в информации, но так более наглядно.

        print(separator,
              'Количество дублирующихся значений: ',
              df.duplicated().sum())

        df.drop_duplicates(inplace=True)                    # Убрать дубликаты записей

        print(separator,
              'Статистика по датасету:\n',
              df.describe())

        df.loc[df.DATE_DIED == '9999-99-99', 'DIED'] = 0    # Признак выживания (Считаем, что выжил, т.к. отсутствует дата смерти)
        df.loc[df.DATE_DIED != '9999-99-99', 'DIED'] = 1    # Признак смерти

        df.info()
        sex_death_visualization(df)
        age_death_visualization(df)
        correlation_visualization(df)
        death_visualization(df)
        medical_unit_visualization(df)

    except Exception as e:
        print(f'При выполнении произошла ошибка: {e}')

