s='BULLBULLBULL'
k=0
m=0

while 'LL' in s and 'BULL' in s:
    if 'LL' in s:
        s=s.replace('BU', 'LL', 1)
        k+=1
    if 'BULL' in s:
        s=s.replace('LLLLLL', 'CAT', 1)
        m+=1
print(k + m)