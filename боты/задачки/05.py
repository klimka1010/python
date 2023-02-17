for n in range(1,100):
    n -= n % 4
    s = bin(n)[2:]

    if s.count('1') % 2 == 0:
        s+='0'
        s='1' + s[2:]    # += лишнее

    else:
        s+='1'
        s='11' + s[2:]   # += лишнее

    r = int(s, 2)
    if r > 56:
        print(n)


#
# for i in range(1, 100):
#     n -= n % 4
#     s = bin(n)[2:]
#     if s.count('1') % 2 == 0:
#         s+='0'