# Дано натуральное число. Требутся определить, является ли год високосным.
# # Если год является високосным, то вывести YES, иначе - NO.
# Високосный год кратен 4 (или 400), но не кратен 100

a = int(input("Введите год: \n"))
if (a % 4 == 0 and a % 400 == 0) or a % 100 != 0:
    print("YES")
else:
    print("NO")