#!/bin/python3
"""
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

- Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

- Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
"""
import timeit
import cProfile


def sieve(idx):
    """
    использование решето Эратосфена
    """
    idx -= 1
    size = 10 * idx
    a = [0] * size
    for i in range(size):
        a[i] = i

    a[1] = 0

    m = 2
    while m < size:
        if a[m] != 0:
            j = m * 2
            while j < size:
                a[j] = 0
                j = j + m
        m += 1

    b = []

    for i in a:
        if a[i] != 0:
            b.append(a[i])

    for i, item in enumerate(b):
        if i == idx:
            return item


def simple_num(idx):
    """
    Класический метод.
    """
    idx -= 1
    simple = [2, ]
    i = 0
    value = 2
    while i < idx:
        value += 1
        for s in simple:
            if value % s == 0:
                break
        else:
            simple.append(value)
            i += 1

    return value


# print('Использование решето Эратосфена')
# print(timeit.timeit('sieve(10)', number=1000, globals=globals()))         # 0.04138671299961061
# print(timeit.timeit('sieve(100)', number=1000, globals=globals()))        # 0.5118247269997482
# print(timeit.timeit('sieve(500)', number=1000, globals=globals()))        # 2.4564535029999206
# print(timeit.timeit('sieve(1000)', number=1000, globals=globals()))       # 5.098031408999759
#
# print('Класический метод.')
# print(timeit.timeit('simple_num(10)', number=1000, globals=globals()))    # 0.008637104000172258
# print(timeit.timeit('simple_num(100)', number=1000, globals=globals()))   # 0.442003110999849
# print(timeit.timeit('simple_num(500)', number=1000, globals=globals()))   # 9.761740491000182
# print(timeit.timeit('simple_num(1000)', number=1000, globals=globals()))  # 39.23197359000005

# print('Использование решето Эратосфена')
# cProfile.run('sieve(1000)')

"""
Использование решето Эратосфена
         1233 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.006    0.006    0.006    0.006 task_4_2.py:27(sieve)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# print('Класический метод.')
# cProfile.run('simple_num(1000)')
"""
Класический метод.
         1003 function calls in 0.053 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.053    0.053 <string>:1(<module>)
        1    0.053    0.053    0.053    0.053 task_4_2.py:59(simple_num)
        1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Проведя аналитику мы увидели что жевя много веков прошлом Эратосфен нашёл метод
# для нахождения простых чисел. а класический метод нас подвел.