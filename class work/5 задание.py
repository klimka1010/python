for n in range (256):
    s = bin(n)[2:] # перевод в двоичную систему
    s = str(s)
    if len(s) < 8:
        s = '0' * (8 - len(s)) + s
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r = int(s, 2) # перевод в десятичную систему
    if r - n == 111:
        print(n)
