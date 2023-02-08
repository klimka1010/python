from itertools import *
def f(x,y,z):
    return (x<=y) and (x or y or (not z)) and ((not x) or z)
for a1,a2,a3 in product([0,1], repeat=3):
    t=[(0,0,0), (0,0,a1), (0,a2,a3)]
    if len(t) == len(set(t)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p,r))) for r in t] == [1,1,1]:
                print(*p, sep='')