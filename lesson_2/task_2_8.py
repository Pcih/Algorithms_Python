"""
https://drive.google.com/file/d/1anUmjPJ1rSyBmQjKiMBIV0o5qbGlvBOl/view?usp=sharing
8. Посчитать, сколько раз встречается определенная цифра в
введенной последовательности чисел.
Количество вводимых чисел и цифра,
которую необходимо посчитать, задаются вводом с клавиатуры.
"""

len_number = int(input("Сколько будет чисел? "))
find_number = int(input("Какую цифру считать? "))
count = 0

for i in range(1, len_number + 1):
    user_number = int(input("Число " + str(i) + ": "))
    while user_number > 0:
        if user_number % 10 == find_number:
            count += 1
        user_number = user_number // 10

print("Было введено %d цифр %d" % (count, find_number))
