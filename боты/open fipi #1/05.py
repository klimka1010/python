a=[]
for N in range(1,100):
    n = bin(N)[2:]
    if int(n) % 2 == 0:
        n = '1' + n + '0'

    if int(n) % 2 != 0:
        n = '11' + n + '11'

    r = int(n, 2)
    if r>255:
        a.append(r)
        print(sorted(a))