def Del(n, m):
    return n % m == 0

for A in range(1,1000):
    pod=True
    for x in range(1,1000):
        if ((Del(x,20) <= (not(Del(x,11)))) or (x + A >=300)) == 0:
            pod = False
            break
    if pod == True:
        print(A)