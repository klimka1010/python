def Del(n, m):
    return n % m == 0


for A in range(1, 1000):
    pod = True
    for x in range(1, 1000):
        if (((Del(x, 13)) <= (not(Del(x, 21)))) or (x + A >= 500)) == False:
            pod = False
            break
    if pod:
        print(A)
