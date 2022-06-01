"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
START_NUM = -50
END_NUM = 200
LEN_NUM = 10


def problem_statement():
    """
    Функция создаёт список для задачи.
    """
    from random import randint
    initial_list = [randint(START_NUM, END_NUM) for _ in range(LEN_NUM)]
    print(f'Созданный список: {initial_list}')
    return initial_list


def find_idx_number(my_list):
    """
     Функция определяет индекс
     минимального числа
    """
    min_number = my_list[0]
    for i in my_list:
        if i < min_number:
            min_number = i
    res_min = my_list.index(min_number)
    return res_min, min_number


def double_min(idx, my_list):
    """
     Функция определяет индекс второго
     минимального числа
    """
    my_list.pop(idx)
    min_number = my_list[0]
    for i in my_list:
        if i < min_number:
            min_number = i
    return min_number


def main():
    list1 = problem_statement()
    a, c = find_idx_number(list1)
    b = double_min(a, list1)
    print(f'Первое минимальное число {c},\n'
          f'Второе минимальное число {b}')
    if c == b:
        print('И они равны.')
    else:
        print('И они не равны.')


if __name__ == "__main__":
    main()
