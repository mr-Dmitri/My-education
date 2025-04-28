def simple_count(s : str) -> int:
    """
    Подсчет длинны строки используя стандартную функцию len().
    :param s : Строка.
    :return  : Длинна строки.
    """
    return len(s)


def main():
    in_str = input("Введите строку: ")          # Запрос ввода строки
    print("Вы ввели:", in_str)                  # Вывод введенной строки
    print(f'Длинна строки составляет '
          f'{simple_count(in_str)} знаков.')    # Вывод длинны введенной строки

if __name__ == '__main__':
    main()