"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

user_number = int(input('Ведите 3-х значное число: '))

first_number = user_number // 100
second_number = (user_number - first_number * 100) // 10
last_number = user_number - (first_number * 100 + second_number * 10)

result_sum = first_number + second_number + last_number
result_product = first_number * second_number * last_number
print(f'Сумма чисел {result_sum}, произведение чисел {result_product}')
