"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

from random import randint
LENGTH = 20
MIN_NUMBER = 0
MAX_NUMBER = 50


def problem_statement():
    list_number = [randint(MIN_NUMBER, MAX_NUMBER) for _ in range(LENGTH)]
    return list_number


def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def main():
    a = problem_statement()
    print(f'Исходный список: \n{a}')
    b = merge_sort(a)
    print(f'Отсартированный список:\n{b}')


if __name__ == '__main__':
    main()
