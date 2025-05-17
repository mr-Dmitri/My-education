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
                                 hue = 'DIED',
                                 figsize=(8, 5)
    )

def gender_death_visualization(df):
    """
    Визуализация смертности по возрасту
    :param df:
    :return:
    """

    # Визуализация смертности по возрасту
    Visualization(df).count_plot(x='DIED',
                                 title='Количество умерших по возрасту.',
                                 ylabel='Количество умерших',
                                 legend=['мужской', 'женский'],
                                 hue='AGE',
                                 figsize=(8, 5)
    )

