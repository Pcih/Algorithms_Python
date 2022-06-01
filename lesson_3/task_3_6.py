"""
6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
START_NUM = -10
END_NUM = 10
LEN_NUM = 20


def problem_statement():
    """
    Функция создаёт список для задачи.
    """
    from random import randint
    initial_list = [randint(START_NUM, END_NUM) for _ in range(LEN_NUM)]
    print(f'Созданный список: {initial_list}')
    return initial_list


def find_idx_number(my_list):
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


def sum_idx(firstnum, secondnam, my_list):
    result = 0

    while firstnum < secondnam:
        result += my_list[firstnum]
        firstnum += 1

    return print(f'Сумма элементов {result}')


def main():
    list_my = problem_statement()
    a, b = find_idx_number(list_my)
    if a < b:
        sum_idx(a+1, b, list_my)
    else:
        sum_idx(b+1, a, list_my)


if __name__ == "__main__":
    main()
