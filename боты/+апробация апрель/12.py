for n in range(1, 1000):
    s = '3' + '5' * n

    while '25' in s or '35' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '3', 1)
        if '35' in s:
            s = s.replace('35', '52', 1)
        if '555' in s:
            s = s.replace('555', '35', 1)
    if s.count('5') == len(s):
        print(n)

