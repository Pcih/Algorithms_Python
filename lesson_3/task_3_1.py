"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9..
"""

START_NUMBER = 2
END_NUMBER = 100
START_DIVIDER = 2
END_DIVIDER = 10


def problem_statement():
    list_number = [i for i in range(START_NUMBER, END_NUMBER)]
    list_divider = [i for i in range(START_DIVIDER, END_DIVIDER)]
    return list_number, list_divider


def multiplicity_search(list1, list2):
    """
    на вход словарь с делителеми
    и списком чисел
    Функция создаёт словарь
    где ключь это делитель
    а значения сколько чисел
    кратных ему в диапозоне
    """
    digit_res = {}
    for number in list1:
        for divider in list2:
            if digit_res.get(divider) is None:
                digit_res[divider] = 1
            elif digit_res.get(divider) is not None and number % divider == 0:
                digit_res[divider] += 1
    return digit_res


def input_digit(digit1):
    """
    Функция принемает словарь
    и возрошает вывод строки:)
    """
    for divider, number in digit1.items():
        print(f'Делителя {divider}, всего в диапозоне {number} чисел.')


def main():
    first, second = problem_statement()
    a = multiplicity_search(first, second)
    input_digit(a)


if __name__ == "__main__":
    main()
