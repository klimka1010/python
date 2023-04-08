from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a * 3, b), (a, b + 1), (a, b * 3)


@lru_cache(None)
def f(h):
    if sum(h) >= 52: return 'end'

    # 19: any any
    # 20: any all any all
    # 21: посмотреть

    if any(f(x) == 'end' for x in moves(h)):
        return 'win1'
    if all(f(x) == 'win1' for x in moves(h)):
        return 'lose1'
    if any(f(x) == 'lose1' for x in moves(h)):
        return 'win2'
    if all(f(x) == 'win2' or f(x) == 'win1' for x in moves(h)):
        return 'lose2'


for i in range(1, 100):
    h = 5, i
    print(h, f(h))
