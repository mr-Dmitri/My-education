import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
    def __init__(self, data_frame):
        self.df = data_frame

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
        print(qargs)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        # ax.legend(qargs.get('legend'))
        # ax.title =
        # ax.set_xlabel(qargs.get('xlabel', ''))
        # ax.set_ylabel(qargs.get('ylabel',''))
        # sns.lineplot(x=x, y=y, **qargs)
        # fig.show()

        plt.figure()
        sns.lineplot(x=self.df[x], y=self.df[y])
        # plt.legend(['<UNK> <UNK>', '<UNK> <UNK>'])
        plt.title(qargs.get('title',''))
        plt.xlabel(qargs.get('xlabel',''))
        plt.ylabel(qargs.get('ylabel',''))
        plt.show()

    def count_plot(self, **qargs):
        plt.figure(figsize=qargs.get('figsize',(8,8)))

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
