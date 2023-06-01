for N in range(1,100):
    n = bin(N)[2:]
    n=str(n)
    if n.count('1') % 2 == 0:
        n='10' + n
    if n.count('1') % 2 != 0:
        n = '1' + n + '01'

    r = int(n,2)

    if N<8:
        print(r)