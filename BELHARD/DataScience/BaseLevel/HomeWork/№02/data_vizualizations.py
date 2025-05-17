import numpy as np
from visualizations import Visualization



def sex_death_visualization(df):
    """
    Визуализация смертности по гендерному признаку
    :param df:
    :return:
    """

    Visualization(df).count_plot(x='SEX',
                                 palette='colorblind',
                                 title ='Количество умерших по гендерному признаку.',
                                 ylabel = 'Количество умерших',
                                 legend = ['мужской','женский'],
                                 hue = 'DIED'
    )

def age_death_visualization(df):
    """
    Визуализация смертности по возрасту
    :param df:
    :return:
    """

    Visualization(df).hist_plot(x='AGE', bins=12)


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

