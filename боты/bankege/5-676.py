for n in range(100):
    s = bin(n)[2:]
    s = str(s)
    if s.count('1') % 2 == 0:
        s+='0'
    else:
        s+='1'
    if s.count('1') % 2 == 0:
        s+='0'
    else:
        s+='1'
    q=int(s,2)
    if q>105:
        print(n)

# 26
