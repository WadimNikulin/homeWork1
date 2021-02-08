def func_sum(strin):
    n = 0
    f = 0
    if strin.count("стоп") == 0:
        while n < len(strin):
            f = f + int(strin[n])
            n += 1
        return f
    elif strin.count("стоп") != 0:
        strin.remove("стоп")
        while n < len(strin):
            f = f + int(strin[n])
            n += 1
        return f


sum1 = 0
flag = True
while flag:
    strin = input("Введите числа через пробел. Когда захотите остановиться напишите 'стоп': ")
    strin = strin.split(" ")
    if strin.count("стоп") == 0:
        sum1 = sum1 + func_sum(strin)
        print(sum1)
    elif strin.count("стоп") != 0:
        sum1 = sum1 + func_sum(strin)
        print(sum1)
        print("Программа закончена! ")
        flag = False
