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