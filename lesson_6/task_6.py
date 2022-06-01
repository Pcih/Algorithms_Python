"""

    Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти (укажите какую задачу вы взяли в комментарии);

● написать 3 варианта кода (один у вас уже есть);

● проанализировать 3 варианта и выбрать оптимальный по суммарной затраченной памяти;

● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

● написать общий вывод: какой из трёх вариантов лучше и почему. 

lesson_3_task1
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Linux pcih-pc 5.13.0-44-generic #49~20.04.1-Ubuntu SMP Wed May 18 18:44:28 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
Python 3.8.10



"""
from sys import getsizeof
from collections import Counter, deque

START_NUMBER = 2
END_NUMBER = 100
START_DIVIDER = 2
END_DIVIDER = 10


def size(data):
    """
    Функция служит для замера используемой памяти.
    """
    print(f'{type(data)=} {getsizeof(data)=} {data=}')
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            sum_key = 0
            sum_value = 0
            for key, value in data.items():
                sum_key += getsizeof(key)
                sum_value += getsizeof(value)
            return f'Сумарный размер всех значений и клчей {sum_key + sum_value} байт.'
        elif hasattr(data, 'index'):
            sum_list = 0
            for i in data:
                sum_list += getsizeof(i)
            return f'Сумарный размер всех значений {sum_list} байт.'


def problem_statement():
    """
    Функция просто создает два списка.
    """
    list_number = [i for i in range(START_NUMBER, END_NUMBER)]
    list_divider = [i for i in range(START_DIVIDER, END_DIVIDER)]
    return list_number, list_divider


def code1(list1, list2):
    """
    Результат функции список.
    """
    result = [0] * len(list2)
    for number in list1:
        for divider in list2:
            if number % divider == 0:
                result[divider - 2] += 1

    return result


def code2(list1, list2):
    """
    Результат функции словарь.
    """
    digit_res = {}
    for number in list1:
        for divider in list2:
            if digit_res.get(divider) is None and number % divider == 0:
                digit_res[divider] = 1
            elif number % divider == 0:
                digit_res[divider] += 1
    return digit_res


def code3(list1, list2):
    """
    Результат функции кортедж.
    """
    result = [0] * len(list2)
    for number in list1:
        for divider in list2:
            if number % divider == 0:
                result[divider - 2] += 1

    return tuple(result)


def code4(list1, list2):
    """
    Результат функции особый вид словорей из библиотеки collections.
    """
    digit_res = {}
    for number in list1:
        for divider in list2:
            if digit_res.get(divider) is None and number % divider == 0:
                digit_res[divider] = 1
            elif number % divider == 0:
                digit_res[divider] += 1
    return Counter(digit_res)


def code5(list1, list2):
    """
    Результат функции особый вид спискас из библиотеки collections.
    """
    result = [0] * len(list2)
    for number in list1:
        for divider in list2:
            if number % divider == 0:
                result[divider - 2] += 1

    return deque(result)


def main():
    a, b = problem_statement()
    print(size(code1(a, b)))
    print(size(code2(a, b)))
    print(size(code3(a, b)))
    print(size(code4(a, b)))
    print(size(code5(a, b)))


if __name__ == '__main__':
    main()

"""
code1 = <class 'dict'>  размер = 120  размер значений =  224
code2 = <class 'dict'>  размер = 360  размер значений и ключей = 448
code3 = <class 'tuple'> размер = 104  размер значений = 224
code4 = <class 'collections.Counter'> размер = 376 размер значений и ключей = 448
code5 = <class 'collections.deque'>   размер = 624  размер значений = 224

Из данных мы видим что победителем оказался кортедж 
но перед тем как выберать как хранить данные всегда 
надо помнить плюсы и минусы тех или иных обектов.
Ради скорости обобработки данных мы можем пожертвовать памятью 
или наоборот. 
"""
