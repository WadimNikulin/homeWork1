def func(x, y):
    s = 1 / x ** y
    return round(s, 10)

x = int(input("Введите число, которое хотите возвести в степень: "))
y = abs(int(input("Введите отрицательное число: ")))

print(func(x, y))