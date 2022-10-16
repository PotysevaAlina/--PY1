money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


def needed_money(month, spend, money_capital, salary):
    while money_capital >= 0 and money_capital >= spend:
        if month == 0:
            spend = spend
        else:
            spend = spend + increase * spend
        money_capital = money_capital + salary - spend
        month = month + 1
    print(month)
needed_money(month, spend, money_capital, salary)
