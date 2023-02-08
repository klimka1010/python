for i in range (2049, 10**10, 2049):
    num = str(i)
    if num[0:2] == '32' and num[3:5] == '21' and num[-1] == '4':
        print(i, i//2049)
