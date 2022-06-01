"""
По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


print('Определяем существует ли треуголник.')
print('И кокого он вида.')

a = int(input('Ведите длину стороны "a": '))
b = int(input('Ведите длину стороны "b": '))
c = int(input('Ведите длину стороны "c": '))

if (a + b) >= c:
    if (b + c) >= a:
        if (c + a) >= b:
            if a == b == c:
                print('Треугольник являеться равностороним.')
            elif a == b or b == c or c == a:
                print('Треугольник являеться равнобедриный.')
            else:
                print('Треугольник являеться разностороний.')
else:
    print('Треугольник не существует.')
