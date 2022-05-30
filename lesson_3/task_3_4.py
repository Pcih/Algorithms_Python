"""
4. Определить, какое число в массиве встречается чаще всего.
"""

START_NUM = 1
END_NUM = 10
LEN_NUM = 50


def problem_statement():
    """
    Функция создаёт список для задачи.
    """
    from random import randint
    initial_list = [randint(START_NUM, END_NUM) for _ in range(LEN_NUM)]
    print(f'Созданный список: {initial_list}')
    return initial_list


def find_number(my_list):
    """
    Функция получает список
    и возращает словарь где
    ключ эта сама цифра а
    значения сколько раз
    всречаеться.
    """
    digit_ras = {}
    for i in my_list:
        if digit_ras.get(i) is None:
            digit_ras[i] = 1
        else:
            digit_ras[i] += 1
    return digit_ras


def find_max_number(my_digit):
    """
    Функция просто ищет ключ
    цифру которая чаще всего
    встречаеться в словоре.
    """
    max_value = 0
    max_idx = 0
    for i, v in my_digit.items():
        if v > max_value:
            max_value = v
            max_idx = i
    return max_idx


def print_resultal(my_digit, idx):
    """
    Просто выводит иформаци.
    """
    print(f'Цифра {idx} встречаеться {my_digit[idx]} раз.')


def main():
    a = problem_statement()
    b = find_number(a)
    find_max_number(b)
    print_resultal(b, find_max_number(b))


if __name__ == "__main__":
    main()
