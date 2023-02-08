from itertools import *
k=0

for x in product('ABCWXYZ', repeat=6):
    s=''.join(x)

    if s.count('W')<=1 and s.count('X')<=1 and s.count('Y')<=1 and s.count('Z')<=1:
        k+=1

print(k)