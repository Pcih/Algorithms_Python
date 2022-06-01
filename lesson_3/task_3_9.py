"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint

START_NUM = 1
END_NUM = 100
DRAINS = 20
COLUMNS = 20


def problem_statement():
    """
    Создаёт матрицу.
    """
    my_matrix = [[randint(START_NUM, END_NUM) for _ in range(COLUMNS)] for _ in range(DRAINS)]
    return my_matrix


def find_element_matrix(matrix):
    """
    Функция вроходит по каждой строки в матрици
    и в ней ищет минимальные числа.
    Потом среди минимального числа находит максимальное.
    """
    min_drains = matrix[0]
    for i in matrix:
        for column_idx, number in enumerate(i):  # Тут можно было расписать при помощи
            if min_drains[column_idx] > number:  # счетчик но я решил испытать новую функцию
                min_drains[column_idx] = number

    max_number = min_drains[0]
    for i in min_drains:
        if max_number < i:
            max_number = i
    return min_drains, max_number


def print_matrix(my_matrix, step=4):
    """
    Просто красивый вывод матрици.
    """
    for i in my_matrix:
        for k in i:
            print(f'{k:>{step}}', end='')
        print()


def main():
    print('Созданная матрица.')
    print_matrix(problem_statement())
    first, second = find_element_matrix(problem_statement())
    print(f'Минималные элементы столбцов\n{first}\n'
          f'максимальный из них {second}')


if __name__ == "__main__":
    main()
