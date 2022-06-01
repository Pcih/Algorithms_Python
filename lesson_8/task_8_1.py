"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9
"""
import hashlib


def sub_str(my_string):
    substring_summ = set()

    for i in range(len(my_string)):
        for j in range(len(my_string), i, -1):
            hash_str = hashlib.sha1(my_string[i:j].encode('utf-8')).hexdigest()
            substring_summ.add(hash_str)
    return len(substring_summ) - 1


def main():
    print(f'Определение количества различных подстрок с использованием хеш-функции')
    string = ''
    while string == '':
        string = input(f'Введите строку: ')
        if len(string) <= 0:
            print(f'Ошибка: Строка не может быть пустой!\n {"*"*50}\nПовторите ввод')
    print('*' * 50)
    print(f'Всего в строке:\n"{string}"\n {sub_str(string)} Различных подстрок')
    print('*' * 50)


if __name__ == '__main__':
    main()