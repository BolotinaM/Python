print(5, 8, 6)

n = 5
m = None
p = 1.89

print(f" {n} -  {m} - {p}") # f-строки

a = "Name \"ha-ha\"" # для вывода кавычек в str надо поставить перед нужной кавычкой \
print(a)

print(type(n)) # выводит тип данных
print("{} - {} - {}".format(n, m, p))


"""
а вот так
комментируются
целые строки в python

а если выделить строки и 
нажать ctrl + k ctrl + c
то закоммитит по #
 ctrl + k ctrl + u - раскоммитит
"""

# input() # ввод данных
print("введите значение аргумента:")
a = input()
b = input("введите второй аргумент:")

print(a, " + ", b, " = ", a + b) 

print("введите значение аргумента:")
a = int(input())
b = int(input("введите второй аргумент:"))

print(a, " + ", b, " = ", a + b)

q = 3.10
print(q)
w = int(q)
print(w)
q = 1
print(q)
print(type(q))
q = bool(q)
print(q)
print(type(q))

e = 3.748484
r = 2.946032
print(e*r)
print(round(e*r, 3))

y = "string"

# print(y[0])
for i in y:
    print(i)

txt = "Это строка для того, чтобы ее форматировать"
print("строка" in txt)
print(txt.lower())
print(txt.upper())
print(txt.replace('для', 'ДЛЯ'))
print(txt[-1]) # обратная индексация
print(txt[:4]) 
print(txt[10:]) 
print(txt[len(txt)-10:]) 
print(txt[0: : 2]) 
print(txt[::2]) 