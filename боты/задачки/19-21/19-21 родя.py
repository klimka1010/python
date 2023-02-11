from functools import lru_cache

# +1, *2
# >= 77
# (8, s), 1 <= s <= 69


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 4, b), (a, b * 4)


@lru_cache(None)
def game(h):
    if sum(h) >= 82:
        return 'w'
    if any(game(m) == 'w' for m in moves(h)):
        return 'p1'
    if all(game(m) == 'p1' for m in moves(h)):
        return 'q1'
    if any(game(m) == 'q1' for m in moves(h)):
        return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(h)):
        return 'q2'


for s in range(1, 78):
    if game((4, s)) is not None:
        print(s, game((4, s)))
