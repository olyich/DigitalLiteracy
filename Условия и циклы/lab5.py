salary = 5000
initial_spend = 6000
months = 10
increase = 0.03

required_capital = 0
current_spend = initial_spend

for month in range(months):
    deficit = current_spend - salary
    required_capital += deficit
    current_spend *= (1 + increase)

required_capital = round(required_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)