"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint

START_NUM = 1
END_NUM = 20
LEN_NUM = 20


def problem_statement():
    """
    Функция создаёт список для задачи.
    """
    initial_list = [randint(START_NUM, END_NUM) for _ in range(LEN_NUM)]
    print(f'Созданный список: {initial_list}')
    return initial_list


def find_idx_number(my_list):
    """
     Функция определяет индекс максимального
     и минимального числа
    """
    max_number = 0
    min_number = my_list[0]
    for i in my_list:
        if i > max_number:
            max_number = i
        elif i < min_number:
            min_number = i
    res_min = my_list.index(min_number)
    res_max = my_list.index(max_number)
    print(f'Максимальное число {max_number} а его индекс {res_max},\n'
          f'Минимальное число {min_number}, а его индекс {res_min}')
    return res_max, res_min


def swap_number(tuple_idx, my_list):
    """
    Функция миняет местами значения по индексу.
    """
    first_number, second_number = tuple_idx
    # first_number = tuple_idx[0]
    # second_number = tuple_idx[1]
    my_list[first_number], my_list[second_number] = my_list[second_number], my_list[first_number]
    return print(f'Именёный список: {my_list}')


def main():
    a = problem_statement()
    b = find_idx_number(a)
    swap_number(b, a)


if __name__ == "__main__":
    main()
