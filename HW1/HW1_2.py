# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = int(input("Сколько всего было сделано журавливов? "))

Kate = int(S // 2)
Sergo = Petya = int(Kate / 2)

if S >= 4:
    if S % 2 != 0:
        Kate = Kate + 1
        print("Катя сделала журавликов: ", Kate) # по условию задачи штрафной журавлик достается ей
        print("Серёжа сделал журавликов: ", Sergo)
        print("Петя сделал журавликов: ", Petya)
    else:
        print("Катя сделала журавликов: ", Kate)
        print("Серёжа сделал журавликов: ", Sergo)
        print("Петя сделал журавликов: ", Petya)
else:
    print("ERROR: не удовлетворяет условиям задачи")