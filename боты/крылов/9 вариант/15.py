def DEL(n,m):
    return n%m == 0

for a in range(1,100):
    pod = True
    for x in range(1,100):
        if ((not(DEL(x,a))) <= (DEL(x,18) <= (not(DEL(x,18))))) == False:
            pod = False
            break

    if pod:
        print(a)
        