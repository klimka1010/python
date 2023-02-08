for n in range(100):
    b=bin(2*n)[2:]
    if bin(n).count('1')>bin(n).count('0'):
        b+='0'
    else:
        b+='11'
        bin(n).count('1') > bin(n).count('0')

    r=int(b, 2)
    print(n, r)