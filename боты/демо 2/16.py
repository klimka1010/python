from functools import *
@lru_cache(None)

def f(n):
    if n<0: return -n
    if n%2==0: return 2*n + 1 + f(n-3)
    if n%2!=0: return 4 * n + 2*f(n-4)


# for i in range(1, 2023+1):
#     f(i)

print(f(33))

# 11612