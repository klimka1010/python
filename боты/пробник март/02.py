import itertools


def f(x, y, z, w):
    return (x <= (not (y <= z))) or w


for x1, x2, x3, x4, x5, x6, x7 in itertools.product([0, 1], reepeat=7):
    t = (
        (x1, 0, x2, 0, 0),
        (1, x3, x4, x5, 0),
        (0, 1, x6, x7, 0)
    )

    if len(t) == len(set(t)):
        for p in itertools.permutation('xyzw', r=4):
            if all(f(**dict(zip(p, ti))) == ti[-1] for ti in t):
                print(*p)
