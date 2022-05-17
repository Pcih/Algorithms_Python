"""
https://drive.google.com/file/d/1anUmjPJ1rSyBmQjKiMBIV0o5qbGlvBOl/view?usp=sharing
3. Сформировать из введенного числа обратное по порядку входящих
в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

У меня 2а решения первое решения при помощи встроиных функций.
Второе решения при помощи рекурсси

Шаги рекурсии.
1) Получаем число от пользователя.
2) обявляем рекурсивную функцию
3) Проверяем условия если длина строки == 1 возрачаем сторку
4) Иначе к стоке прибовляем вызов функции + срех в обратом порядке
"""
print('Програма подщитывает из веденной вами числа сколько в нем четных и нечетных цифр.')

user_mode = input('Два режима: \n'
                  '1. Припомощи встроиных функций:\n'
                  '2. При помощи рекурсии и срезов:\n'
                  '3. При помощи рекурсии расчетов:\n'
                  'Выбери режим: ')
user_number = input('Ведите целое натуральное число мин 3х значное: ')


def my_reversed_str(string):
    if len(string) == 1:
        return string
    return string[-1] + my_reversed_str(string[:-1])


def my_reversed(a, b=True):
    if a == 0:
        return f''
    if a % 10 == 0 and b is True:
        return my_reversed(a // 10, True)
    return f'{a % 10}{my_reversed(a // 10, False)}'


if user_mode == '1':
    print(int(''.join(reversed(user_number))))

elif user_mode == '2':
    result = int(my_reversed_str(user_number))
    print(result)

elif user_mode == '3':
    result = my_reversed(int(user_number))
    print(result)
else:
    print('Нет такого режима!')
