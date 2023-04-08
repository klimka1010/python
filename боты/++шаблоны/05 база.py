# найти N
def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n += '10'
    else:
        n = '1' + n + '01'
    return int(n, 2)


for N in range(1, 9):
    print(f(N))



# найти R
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
    r=int(s,2)
    if r>105:
        print(n)
