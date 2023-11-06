s='1'*38+'2'*34+'3'*30
a=[]
while '33' in s or '11' in s or '22' in s:
    if '33' in s:
        s=s.replace('33','12',1)
    if '11' in s:
        s=s.replace('11','32',1)
    if '22' in s:
        s=s.replace('22','31',1)

print(sum(map(int,s)))