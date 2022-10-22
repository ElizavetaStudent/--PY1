money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить
# TODO Оформить решение
growth = 1.05
y = salary - spend
while money_capital + y >= spend:
    money_capital += y
    spend = spend * growth
    month += 1

print(month)