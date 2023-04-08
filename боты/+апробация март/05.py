def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n += '10'
    else:
        n = '1' + n + '01'
    return int(n, 2)


for N in range(1, 9):
    print(f(N))
