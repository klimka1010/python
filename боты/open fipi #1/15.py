def Del(n, m):
    return n % m == 0

b=range(50,70)
for a in range(1, 100):
    pod = True
    for x in range(1, 100):
        if (Del(x, a) or ((x in b) <= (not (Del(x, 16))))) == False:
            pod = False
    if pod:
        print(a)
