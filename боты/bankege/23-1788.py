def f(n, c):
    if n > c: return 0
    if n == c: return 1
    if n < c: return f(n + 1, c) + f(n + 2, c) + f(n * 2, c)


print(f(4, 11) * f(11, 14))

# [4; 11] * [11; 14] == {11}
