def f(n, end):
    if n == end: return 1
    if n < end: return 0
    return f(n + 1, end) + f(n * 2, end) + f(n * 3, end)


print(f(1, 32) * f(12, 14) * f(15, 32))
