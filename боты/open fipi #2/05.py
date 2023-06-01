for N in range(1, 100):
    n = bin(N)[2:]
    if int(n) % 2 == 0:
        n = '1' + n + '00'
    else:
        n = n

    r = int(n, 2)
    if r>190:
        print(r)