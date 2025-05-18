import numpy as np
from visualizations import Visualization



def sex_death_visualization(df):
    """
    Визуализация смертности по гендерному признаку
    :param df:
    :return:
    """
    df_tmp = df.copy()
    df_tmp['SEX'] = df_tmp['SEX'].map({1: 'Женщины', 2: 'Мужчины'})
    Visualization(df_tmp).count_plot(x='SEX',
                                 palette='colorblind',
                                 title ='Количество умерших по гендерному признаку.',
                                 ylabel = 'Количество',
                                 legend = ['Выжили','Умерли'],
                                 hue = 'DIED'
    )

def age_death_visualization(df):
    """
    Визуализация смертности по возрасту
    :param df:
    :return:
    """

    Visualization(df).hist_plot(x='AGE',
                                bins=12,
                                title ='Количество умерших в возрасте.',
                                xlabel= 'Возраст',
                                ylabel = 'Количество умерших',
                                )


def correlation_visualization(df):
    """
    Визуализация корреляции параметров

    :param df:
    :return:
    """
    corr = df.drop(columns=['DATE_DIED','DIED']).corr()
    mask = np.triu(np.ones_like(corr), k=-1)

    Visualization(df).heatmap_plot(data = corr,
                                   title='Тепловая карта корреляции параметров',
                                   mask=mask,
                                   annot=True,
                                   cmap='Blues',
                                   vmin=-1,
                                   vmax=1,
                                   figsize = (20,15)
    )

def death_visualization(df):
    """
    Визуализаця умерших и выживших

    :param df:
    :return:
    """
    data = df['DIED'].value_counts()
    labels = list(df['DIED'].value_counts().index)
    labels = ['Выжили' if i == 0 else 'Умерли' for i in labels]
    Visualization(df).pie_plot(data=data,
                               legend=labels,
                               title='Количество умерших и выживших',
                               autopct ='%1.2f%%',
                               figsize=(5,5)
    )

def d_visualization(df):
        """
        Визуализаця результатов теста на covid в учреждении
        Национальной системы здравоохранения типа 7
        у пациентов в возрасте от 30 до 60 лет.

        :param df:
        :return:
        """
        # df_f = df[(df['AGE'] == 40)]
        # df_f = df[(df['AGE'] >= 10) & (df['AGE'] <= 15) & (df['ASTHMA'] < 90)]
        # df_f = df[(df['AGE'] >= 40) & (df['AGE'] <= 60) & (df['CLASIFFICATION_FINAL'] > 4)]
        df_f = df[df['MEDICAL_UNIT'] == 7 & (df['AGE'] >= 30) & (df['AGE'] <= 60)]
        Visualization(df_f).scatter_plot(data=df,
                                         title='Результаты теста на covid\nв учреждении '
                                               'Национальной системы здравоохранения типа 7\n'
                                               'у пациентов в возрасте от 30 до 60 лет',
                                         y=df_f['AGE'],
                                         x=df_f['CLASIFFICATION_FINAL'],
                                         figsize=(9,7),
                                         xlabel= 'Результаты теста на covid\n1...3 - у пациента был диагностирован covid в разной степени;\n4 или выше - пациент не является носителем covid или тест не дал результатов.',
                                         ylabel= 'Возраст'
        )

