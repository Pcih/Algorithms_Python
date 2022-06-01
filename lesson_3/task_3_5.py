"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и
«максимальный отрицательный». Это два абсолютно разных значения.
"""


START_NUM = - 10
END_NUM = 5
LEN_NUM = 20


def problem_statement():
    """
    Функция создаёт список для задачи.
    """
    from random import randint
    initial_list = [randint(START_NUM, END_NUM) for _ in range(LEN_NUM)]
    print(f'Созданный список: {initial_list}')
    return initial_list


def find_max_number(my_list):
    max_namber = - abs(my_list[0])
    for i in my_list:
        if max_namber < i < 0:
            max_namber = i
    print(f'Максимальный отрицательный элемент в масиве {max_namber}\n'
          f'Его индекс в масиве {my_list.index(max_namber)}')
    return max_namber, my_list.index(max_namber)


def main():
    a = problem_statement()
    find_max_number(a)


if __name__ == "__main__":
    main()