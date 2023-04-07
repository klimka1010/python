def f(x, end):
    if x < end: return 0
    if x == end: return 1
    return f(x - 1, end) + f(x // 2, end)


# 1620
print(f(50, 10) * f(10, 1))
