import numpy as np


def simple_count(s: str) -> int:
    """
    Подсчет длинны строки используя стандартную функцию len().

    :param s : Строка.
    :return  : Длинна строки.
    """
    return len(s)


def count_by_symbol(s: str) -> int:
    """
    Подсчет длинны строки используя преобразование ее в массив
    и подсчет количества элементов массива.

    :param s : Строка.
    :return  : Длинна строки.
    """
    return len(list(s))


def get_str_statistic(s:str):
    """
    Функция посчета статистики символов в строке

    :param s: Строка
    :return: Словарь, где:
              count - общее количество символа в строке;
              uniq  - количество не повторяющихся символов;
              stat  - посимвольная статистика, где:
                  sym         - символ;
                  sym_count   - количество повторений символа в строке;
                  percentages - процент повторений символа в строке.
    """

    ch_arr = np.array(list(s))                              # Преобразование строки в массив символов
    len_arr = len(ch_arr)

    uniq_ch, counts = np.unique(ch_arr, return_counts=True) # Использую np.unique для подсчета уникальных символов и их количества
    stat = [{'sym':str(char),
             'sym_count':int(count),
             'percentages':round((count/len_arr)*100,2)}
            for char, count in zip(uniq_ch, counts)]        # Словарь со статистикой по каждому символу
    return {'count':len_arr,
            'uniq':len(uniq_ch),
            'stat':stat}



def main():
    in_str = input("Введите строку: ")                                          # Запрос ввода строки
    print("Вы ввели:", in_str)                                                  # Вывод введенной строки

    print('\nПростой подсчет длинны строки.')
    print(f'Длинна строки составляет '
          f'{simple_count(in_str)} знаков.')                                    # Вывод длинны введенной строки, используя простой подсчет

    print('\nПодсчет длинны строки с использованием массива')
    print(f'Длинна строки составляет '
          f'{count_by_symbol(in_str)} знаков.')                                 # Вывод длинны введенной строки, используя преобразование в массив и посчет количества элементов массива


    stat = get_str_statistic(in_str)                                            # Получить посимвольную статистику
    print('\nПосимвольная статистика введенной строки.')                        # Далее вывод посимвольной статистики
    print(f'Общее количество символов в строке: {stat.get('count')}.')
    print(f'Количество уникальных символов в строке: {stat.get('uniq')}.')
    [print(f'Символ: "{i.get('sym')}", '
           f'количество повтроений: {i.get('sym_count')}'
           f', процент повторений: {i.get('percentages')}')
        for i in stat.get('stat')]

if __name__ == '__main__':
    main()
