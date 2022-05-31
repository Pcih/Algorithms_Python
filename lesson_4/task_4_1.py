#!/bin/python3
"""
1.  Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

# Пример из 3.2  Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# Использую цикл while и счечик.

import random
import timeit
import cProfile

min_num = 1
max_num = 99


def problem_statement(long_list=20):
    """
     Функция создаёт рандомный список.
    """
    initial_list = [random.randint(min_num, max_num) for _ in range(long_list)]
    return initial_list


def fun_find_idx_case_1(list_fun):
    """
    Использование простого счетчика.
    """
    k = 0
    list_res = []
    for i in list_fun:
        if i % 2 == 0:
            list_res.append(k)
        k += 1
    return list_res


def fun_find_idx_case_2(list_fun):
    """
    Второй вариант это использование встроенной функции index().
    """
    list_res = []
    for n in list_fun:
        if n % 2 == 0:
            list_res.append(list_fun.index(n))
    return list_res


def fun_find_idx_case_3(list_fun):
    """
    Второй вариант это использование встроенной функции enumerate().
    """
    list_res = []
    for idx, num in enumerate(list_fun):
        if num % 2 == 0:
            list_res.append(idx)
    return list_res

# print('timeit case 1:')
# print(timeit.timeit('fun_find_idx_case_1(problem_statement(1000))', number=1000, globals=globals())) # 0.9725421387702227
# print(timeit.timeit('fun_find_idx_case_1(problem_statement(2000))', number=1000, globals=globals())) # 2.8528669141232967
# print(timeit.timeit('fun_find_idx_case_1(problem_statement(3000))', number=1000, globals=globals())) # 5.603827575221658
# print(timeit.timeit('fun_find_idx_case_1(problem_statement(4000))', number=1000, globals=globals())) # 8.45472758077085
#
# print('timeit case 2:')
# print(timeit.timeit('fun_find_idx_case_2(problem_statement(1000))', number=1000, globals=globals())) # 1.517730213701725
# print(timeit.timeit('fun_find_idx_case_2(problem_statement(2000))', number=1000, globals=globals())) # 4.5678280889987946
# print(timeit.timeit('fun_find_idx_case_2(problem_statement(3000))', number=1000, globals=globals())) # 9.282267712056637
# print(timeit.timeit('fun_find_idx_case_2(problem_statement(4000))', number=1000, globals=globals())) # 14.03956682793796
#
# print('timeit case 3:')
# print(timeit.timeit('fun_find_idx_case_3(problem_statement(1000))', number=1000, globals=globals())) # 0.9622511547058821
# print(timeit.timeit('fun_find_idx_case_3(problem_statement(2000))', number=1000, globals=globals())) # 2.8252856824547052
# print(timeit.timeit('fun_find_idx_case_3(problem_statement(3000))', number=1000, globals=globals())) # 5.608649266883731
# print(timeit.timeit('fun_find_idx_case_3(problem_statement(4000))', number=1000, globals=globals())) # 8.41599596478045
#
# print('cProfile case 1:')
# cProfile.run('fun_find_idx_case_1(problem_statement(10000))')


"""
cProfile case 1:
         52096 function calls in 0.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
     9000    0.005    0.000    0.012    0.000 random.py:200(randrange)
     9000    0.003    0.000    0.014    0.000 random.py:244(randint)
     9000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.017    0.017 task_4_1.py:27(problem_statement)
        1    0.003    0.003    0.017    0.017 task_4_1.py:31(<listcomp>)
        1    0.002    0.002    0.002    0.002 task_4_1.py:35(fun_find_idx_case_1)
        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
     4451    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     9000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    11639    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# print('cProfile case 2:')
# cProfile.run('fun_find_idx_case_2(problem_statement(10000))')

"""
cProfile case 2:
         56505 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
     9000    0.005    0.000    0.012    0.000 random.py:200(randrange)
     9000    0.003    0.000    0.014    0.000 random.py:244(randint)
     9000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.017    0.017 task_4_1.py:27(problem_statement)
        1    0.003    0.003    0.017    0.017 task_4_1.py:31(<listcomp>)
        1    0.002    0.002    0.008    0.008 task_4_1.py:48(fun_find_idx_case_2)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
     4405    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     9000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    11689    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
     4405    0.006    0.000    0.006    0.000 {method 'index' of 'list' objects}

"""
# print('cProfile case 3:')
# cProfile.run('fun_find_idx_case_3(problem_statement(10000))')

"""
cProfile case 3:
         52057 function calls in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
     9000    0.005    0.000    0.011    0.000 random.py:200(randrange)
     9000    0.003    0.000    0.014    0.000 random.py:244(randint)
     9000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.016    0.016 task_4_1.py:27(problem_statement)
        1    0.002    0.002    0.016    0.016 task_4_1.py:31(<listcomp>)
        1    0.001    0.001    0.002    0.002 task_4_1.py:59(fun_find_idx_case_3)
        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
     4447    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     9000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    11604    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# https://docs.google.com/spreadsheets/d/1nCWGy5vX23Xy_haDEjuleJ9szwoR8i8kNogzx44rxvg/edit?usp=sharing?
#
# В первом случае я использовал простой счетчик во втором случае я для добавления индекса в словарь
# я использовал встроенную функуию index() и для последнего случая я использовал функцию enumerate()
#
# Timeit показал что по времени добавления в список припомощи функции index() замедляет скрипт
# так же cProfile показал лишние вызывы функции index() я думаю что при работе с большими данными
# не стоит вызывать функцию в функции.
# между первым и третим примером я не увидел особый разници но на мой взгляд 3 пример выглидит приятний.
