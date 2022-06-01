"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
from random import randint

LENGTH = 15
MIN_NUMBER = -100
MAX_NUMBER = 100


def problem_statement():
    list_number = [randint(MIN_NUMBER, MAX_NUMBER) for _ in range(LENGTH)]
    return list_number


def bubble_sort(res_listy):
    """
    Пузерёк поплыл вверх.
    """
    n = 1
    while n < len(res_listy):
        for i in range(len(res_listy) - n):
            if res_listy[i] > res_listy[i + 1]:
                res_listy[i], res_listy[i + 1] = res_listy[i + 1], res_listy[i]
        n += 1
    return res_listy


def main():
    a = problem_statement()
    print(f'Исходный список: \n{a}')
    b = bubble_sort(a)
    print(f'Отсартированный список:\n{b}')


if __name__ == '__main__':
    main()
