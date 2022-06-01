"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""


import random

MIN_ITEM = 0
MAX_ITEM = 10
rand = random.randint(MIN_ITEM, MAX_ITEM)
array = [random.randint(0, i) for i in range((2 * rand) + 1)]

print(array)
print(sorted(array))
print('=' * 60)


def median(data):
    middle = len(data) // 2
    data.sort()
    if not len(data) % 2:
        return (data[middle - 1] + data[middle]) / 2.0
    return data[middle]


print(f'Медиана равна = {median(array)}')