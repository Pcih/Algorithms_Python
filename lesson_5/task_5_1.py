"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict


def company_enter():
    """
    Функция создаёт словарь с исходными данными.
    """
    quarter = 4
    company_profit = defaultdict(list)
    count_company = int(input("Введите кол-во компаний: "))
    for i in range(count_company):
        company_name = input(f'Введите название {i + 1}-й компании: ')
        for j in range(quarter):
            company_profit[company_name].append(int(input(f'Введите прибыль компании за {j + 1}-й квартал: ')))
    return company_profit


def average_cost(company_digit):
    """
    Функция ведёт ращет средней прыбыли и убыточных и прибыльных предприятий.
    """
    average_profit = (sum(sum(value) for value in company_digit.values())) / len(company_digit)
    print(f'Средняя прибыль: {average_profit}')
    digit_profitable_company = {'Прибыльные компании': [], 'Убыточные компании': [], 'Вышли в 0': []}
    for name, value in company_digit.items():
        profit = sum(value)
        if profit > average_profit:
            digit_profitable_company['Прибыльные компании'].append(name + f'({profit})')
        elif profit < average_profit:
            digit_profitable_company['Убыточные компании'].append(name + f'({profit})')
        else:
            digit_profitable_company['Вышли в 0'].append(name + f'({profit})')
    for key, val in digit_profitable_company.items():
        print(f'{key}: {", ".join(val)}')


def main():
    res_digit = company_enter()
    average_cost(res_digit)


if __name__ == '__main__':
    main()
