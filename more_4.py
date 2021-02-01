n = float(input(" Введите целое положительное число: "))
answer = 0
while n != 0:
    m = n % 10
    if m > answer:
        answer = m
    n //= 10
print("Самая большая цифра: ", int(answer))