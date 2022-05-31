"""
2. Написать программу сложения и умножения двух положительных целых
шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл
A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


BASE = 16
value2digit = dict(enumerate('0123456789ABCDEF'))
digit2value = {v: k for k, v in value2digit.items()}


def long_hex_sum(a, b):
    """
    Функция вычесляет сумму двух чисел.
    """
    max_len = len(a) if len(a) > len(b) else len(b)
    n = a.copy()
    n.extendleft(['0'] * (max_len + 1 - len(a)))
    m = b.copy()
    m.extendleft(['0'] * (max_len + 1 - len(b)))
    sum_deque = deque(['0'] * (max_len + 1))
    overflow = 0
    for pos in range(len(sum_deque) - 1, -1, -1):
        digit_sum = digit2value[n[pos]] + digit2value[m[pos]] + overflow
        sum_deque[pos] = value2digit[digit_sum % BASE]
        overflow = digit_sum // BASE
    while len(sum_deque) > 1 and sum_deque[0] == '0':
        sum_deque.popleft()
    return sum_deque


def long_hex_prod(a, b):
    """
    Функция вычесляет произведение двух чисел.
    """
    multiplication_deque = deque([0] * (len(a) + len(b)))
    for i, a_digit in zip(range(len(a)-1, -1, -1), a):
        for j, b_digit in zip(range(len(b)-1, -1, -1), b):
            pos = i + j + 1
            multiplication_deque[-pos] += digit2value[a_digit] * digit2value[b_digit]
            while pos < len(multiplication_deque) and multiplication_deque[-pos] >= BASE:
                multiplication_deque[-pos-1] += multiplication_deque[-pos] // BASE
                multiplication_deque[-pos] = multiplication_deque[-pos] % BASE
                pos += 1
    multiplication_deque = deque([value2digit[d] for d in multiplication_deque])
    while len(multiplication_deque) > 1 and multiplication_deque[0] == '0':
        multiplication_deque.popleft()
    return multiplication_deque


def main():
    first_number = deque(input("Введите 1-е шестнадцатеричное число: ").upper())
    second_number = deque(input("Введите 2-е шестнадцатеричное число: ").upper())
    summa = long_hex_sum(first_number, second_number)
    multiplication = long_hex_prod(first_number, second_number)
    print(f"Сумма = {list(summa)}")
    print(f"Произведение = {list(multiplication)}")


if __name__ == '__main__':
    main()
