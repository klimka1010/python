from itertools import *
def f(x,y,z,w):
    return (not(x<=z)) or (y==w) or y
for a1,a2,a3,a4,a5,a6 in product([0,1], repeat=6):
    t=[(0,0,a1,a2), (0,a3,a4,a5), (1,1,a6,0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
                print(*p, sep='')


# xzwy