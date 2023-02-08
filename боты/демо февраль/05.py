for n in range(100):
    b = bin(2 * n)[2:]
    if bin(n).count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    if bin(n).count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    r = int(b, 2)
    print(n, r)
