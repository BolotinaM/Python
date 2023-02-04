# Найдите сумму цифр трехзначного числа

a = int(input("Введите трехзначное число: "))
str_a = str(a)
sum = 0

if len(str_a) != 3:
    print("ERROR: число не является трехзначным")
else:
    while (a != 0):
        sum = sum + a % 10
        a = a // 10
    print("Ответ: ", sum)