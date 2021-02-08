def my_share(arg_1, arg_2):
    if b != 0:
        c = a / b
        c = round(c, 3)
        return c
    elif b == 0:
        er = print("На ноль делить нельзя!")
        return er


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(my_share(a, b))
