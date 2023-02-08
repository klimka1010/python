from itertools import *

def f(x,y,z,w):

    return not(w<=z) or (x<=y) or (not x)

for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):

    t=[(a1,1,0,1), (1,1,a2,a3), (a4,a5,a6,1)]

    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:

                print(*p, sep='')