def f(n, m):
    return n % m == 0


def fun(x, A):
    return (f(x, 2) <= (not f(x, 3))) or (x + A >= 100)


print(min(A for A in range(1, 100) if all(fun(x, A) for x in range(1, 1000))))
