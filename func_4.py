def func(x, y):
    n = 1
    p = x
    while n < y:
        p = p * x
        n += 1
    s = 1 / p
    return round(s, 10)


x = int(input("Введите число, которое хотите возвести в степень: "))
y = abs(int(input("Введите отрицательное число: ")))

print(func(x, y))