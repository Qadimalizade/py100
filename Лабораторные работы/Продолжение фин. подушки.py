salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
count = 0
money_capital = 0

while count < months:
    money_capital += spend - salary
    spend += increase * spend
    count += 1
money_capital = round(money_capital)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
