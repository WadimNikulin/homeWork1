def func_sum_max(a, b, c):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    w = min(list)
    list.remove(w)
    sum = list[0] + list[1]
    return sum

a = int(input("Введите целое число: "))
b = int(input("Введите целое число: "))
c = int(input("Введите целое число: "))

print(func_sum_max(a, b, c))
