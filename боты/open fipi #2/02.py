from itertools import *
def f(x,y,z,w):
    return (not(y <= (x == w))) and (z<=x)
for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
    t=[(a1,1,1,a2), (0,a3,a4,0), (a5,0,1,0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [1,1,1]:
                print(*p, sep='')

