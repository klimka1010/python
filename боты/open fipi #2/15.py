def Del(n, m):
    return n % m == 0

for a in range(1,100):
    pod = True
    for x in range(1,1000):
        if ((Del(x,2) <= (not(Del(x,3)))) or (x+a>=100)) == False:
            pod = False
            break
    if pod:
        print(a)
