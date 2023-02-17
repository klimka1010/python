# поразрядная конъюнкция
for A in range(0, 1000):
    Apodoshel = True
    for x in range(0, 1000):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))) == False:
            Apodoshel = False
            break  # выходим при первом не подходящем случае
    if Apodoshel:
        print(A)


# ДЕЛ  ищем обратное True/False     for/else конструкция
def Del(n, m):
    return n % m == 0


for A in range(1, 1000):
    for x in range(1, 1000):
        if ((not (Del (x, A))) <= (Del(x, 6) <= (not(Del(x, 9))))) == False:
            break
    else:
        print(A)


# задача на графики (x,y)  for/else не подходит
for A in range(1, 1000):
    pod = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((2 * x + y != 70) or (x < y) or (A < x)) == False:
                pod = False
                break
        if pod == False:
            break
    if pod == True:
        print(A)


# ДЕЛ х,у   for/else
def Del(n, m):
    return n % m == 0

for A in range(1,1000):
    for x in range(1, 1000):
        if ((Del(x,2) <= (not(Del(x,3)))) or (x+A>=100)) == False:
            break
    else:
        print(A)


# задача на отрезки     принадлежит 'in', не принадлежит 'not in'
D = list(range(17, 58 + 1))  # создание диапазона (списка)
C = list(range(29, 80 + 1))
A = []

for x in range(1, 100):
    if ((x in D) <= (((not (x in C)) and (not (x in A))) <= (not (x in D)))) == False:
        A.append(x)  # наименьшая длина
print(A)  # из большего вычесть меньшее A[-1] - A[0]


# задача на отрезки 2
P = list(range(3, 13 + 1))
Q = list(range(12, 22 + 1))
A = list(range(1, 100))

for x in range(1, 100):
    if (((x in A) <= x in P) or (x in Q)) == False:
        A.remove(x)  # (наибольшая длина)
print(A)  # 19
