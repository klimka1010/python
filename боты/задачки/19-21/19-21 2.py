from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h) >= 181:
        return 'w'
    if any(game(m) == 'w' for m in moves(h)):
        return 'p1'
    if all(game(m) == 'p1' for m in moves(h)):
        return 'q1'
    if any(game(m) == 'q1' for m in moves(h)):
        return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(h)):
        return 'q2'


for s in range(1, 180):
    if game((s)) is not None:
        print(s, game((s)))
