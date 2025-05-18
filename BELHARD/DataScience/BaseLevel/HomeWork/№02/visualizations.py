import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, data_frame):
        self.df = data_frame
        self.def_size = (8,5)

    def line_plot(self, x, y, **qargs) -> None:
        """
        Линейный график
        Входные переменные данных; должны быть числовыми.
        Можно передавать данные напрямую или ссылаться на столбцы в данных.

        :param x: Входная переменная данных.
        :param y: Входная переменная данных.
        :param title: Название
        :param xlabel: Подпись оси X.
        :param ylabel: Подпись оси Y.
        """
        plt.figure(figsize=qargs.get('figsize', self.def_size))

        plt.figure()
        sns.lineplot(x=self.df[x], y=self.df[y])
        plt.title(qargs.get('title',''))
        plt.xlabel(qargs.get('xlabel',''))
        plt.ylabel(qargs.get('ylabel',''))
        plt.show()

    def count_plot(self, **qargs):
        """
        Столбчатуая диаграмма

        :param qargs:
        :return:
        """
        plt.figure(figsize=qargs.get('figsize',self.def_size))

        sns.countplot(data=self.df,
                      x=qargs.get('x'),
                      palette=qargs.get('palette', 'colorblind'),
                      hue=self.df[qargs.get('hue')] if 'hue' in qargs else None
        )
        plt.title(qargs.get('title',''))
        plt.xlabel(qargs.get('xlabel',''))
        plt.ylabel(qargs.get('ylabel',''))
        plt.legend (qargs.get('legend',[]))
        plt.show()


    def hist_plot(self, **qargs):
        """
        Гистограмма
        :param qargs:
        :return:
        """
        plt.figure(figsize=qargs.get('figsize', self.def_size))

        sns.histplot(data=self.df,
                     x=qargs.get('x'),
                     y=qargs.get('y'),
                     kde=qargs.get('kde', False),
                     bins=qargs.get('bins',  'auto'),
                     palette=qargs.get('palette'),
                     hue=self.df[qargs.get('hue')] if 'hue' in qargs else None
        )
        plt.title(qargs.get('title',''))
        plt.xlabel(qargs.get('xlabel',''))
        plt.ylabel(qargs.get('ylabel',''))
        plt.legend (qargs.get('legend',[]))
        plt.show()


    def bar_plot(self, **qargs):
        plt.figure(figsize=qargs.get('figsize', self.def_size))


    def heatmap_plot(self, **qargs):
        """
        Тепловая карта

        :param qargs:
        :return:
        """
        fig, ax = plt.subplots(figsize=qargs.get('figsize', self.def_size))
        sns.heatmap(
                    data=qargs.get('data', None),
                    annot=True,
                    mask=qargs.get('mask', None),
                    cmap=qargs.get('cmap', None),
                    vmin=qargs.get('vmin', None),
                    vmax=qargs.get('vmax', None),
                    ax=ax,

        )
        plt.title(qargs.get('title',''))
        plt.xlabel(qargs.get('xlabel',''))
        plt.ylabel(qargs.get('ylabel',''))

        plt.show()

    def pie_plot(self, **qargs):
        """
        Тепловая карта

        :param qargs:
        :return:
        """
        data = qargs.get('data', None)
        plt.figure(figsize=qargs.get('figsize', self.def_size))
        plt.pie(data,

                labels=qargs.get('labels', None),
                autopct=qargs.get('autopct'))

        plt.title(qargs.get('title',''))
        plt.legend(qargs.get('legend',''))

        plt.show()

    def scatter_plot(self, **qargs):
        """
        Диаграмма рассеивания

        :param qargs:
        :return:
        """
        plt.figure(figsize=qargs.get('figsize', self.def_size))

        sns.scatterplot(data=self.df,
                     x=qargs.get('x'),
                     y=qargs.get('y'),
                     palette=qargs.get('palette'),
                     hue=self.df[qargs.get('hue')] if 'hue' in qargs else None
                     )
        plt.title(qargs.get('title', ''))
        plt.xlabel(qargs.get('xlabel', ''))
        plt.ylabel(qargs.get('ylabel', ''))
        plt.legend(qargs.get('legend', []))
        plt.show()
