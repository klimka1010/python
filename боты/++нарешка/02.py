from itertools import *
def f(x,y,z,w):
    return (not(y<=z)) or ((not(x))<=(not(w))) or x

for a1,a2,a3,a4,a5,a6 in product([0,1], repeat = 6):
    t=[(a1,a2,a3,0), (0,a4,a5,0), (0,a6,0,0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
                print(*p)