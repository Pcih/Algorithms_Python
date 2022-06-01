"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""


def new_matrix():
    """
    Функция заполняет мартицу
    """
    print("Заполним матрицу в начале ведём количество строк в матрице\n"
          "в каждую строку через пробел заполняем значениями.")
    mas = [list(map(int, input(f'Ведите числа в сторке {i+1}: ').split()))
           for i in range(int(input('Ведите количесто строк: ')))]
    return mas


def sum_matrix(my_matrix):
    """
    Функция принемает матрицу делает сумму строк
    и возращает мартрицу с подщетом
    """
    for i in my_matrix:
        sum_line = 0
        for k in i:
            sum_line += k
        i.append(sum_line)
    return my_matrix


def print_matrix(my_matrix, step=4):
    """
    Просто красивый вывод матрици.
    """
    for i in my_matrix:
        for k in i:
            print(f'{k:>{step}}', end='')
        print()


def main():
    a = sum_matrix(new_matrix())
    print_matrix(a)


if __name__ == "__main__":
    main()
