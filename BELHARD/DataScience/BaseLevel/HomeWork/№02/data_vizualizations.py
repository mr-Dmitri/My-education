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


