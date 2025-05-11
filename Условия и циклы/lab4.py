money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Счетчик месяцев

while True:
    # Доступные средства в текущем месяце
    available = money_capital + salary

    # Если средств хватает на текущие расходы
    if available >= spend:
        money_capital = available - spend  # Обновляем подушку безопасности
        spend *= (1 + increase)  # Увеличиваем расходы на следующий месяц
        months += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)