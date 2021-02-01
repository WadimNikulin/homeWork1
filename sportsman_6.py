resultOneDay = float(input("Введите результат первого дня: "))
resultLastDay = float(input("Введите желаемый результат: "))
print(1, "день", '{:.2f}'.format(resultOneDay))
day = 2
while resultLastDay > resultOneDay:
    resultOneDay = resultOneDay + (resultOneDay * 0.1)
    print(day, "день", '{:.2f}'.format(resultOneDay))
    day += 1
