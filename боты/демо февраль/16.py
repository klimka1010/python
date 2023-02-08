from functools import *
@lru_cache(None)
def f(n):
    if n==1: return 1
    else: return n*f(n-1)

for i in range(1, 2023+1):
    f(i)

print(int((f(2023)-f(2022))/f(2020)))