"""
https://drive.google.com/file/d/1anUmjPJ1rSyBmQjKiMBIV0o5qbGlvBOl/view?usp=sharing
5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

Решение с помощю цикла:
1) обявляем начальный символ строки и счечик
2) код переобразуем в символ
3) символ прибавляем к строке
4) через 10 символов делаем перевод на новую строку

Решение с помощю рекурсии:

"""


start_sim = 32
stop_sim = 127
paragraph = 10
i = 0
text_end = ''

while start_sim != stop_sim:
    if i % paragraph == 0:
        text_end += '\n'
        i += 1
        start_sim += 1
    else:
        text_end += (chr(start_sim) + ',')
        i += 1
        start_sim += 1
print(text_end)
