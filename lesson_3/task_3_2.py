"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

# Функция для создания списка.
# def problem_statement():
#     from random import randint
#     initial_list = [randint(1, 100) for _ in range(20)]
#     print(initial_list)
#     return initial_list


initial_list = [100, 25, 14, 50, 46, 96, 33, 9, 96, 40, 88, 6, 45, 42, 34, 75, 45, 52, 41, 24]


def fun_find_idx(list_fun):
    """
    Принемает список натуральных чисел
    возращает список с индексами
    где четные числа.
    """
    k = 0
    list_res = []
    for i in list_fun:
        if i % 2 == 0:
            list_res.append(k)
        k += 1
    return list_res


def main():
    print(fun_find_idx(initial_list))


if __name__ == "__main__":
    main()

