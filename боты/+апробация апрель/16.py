from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 2024: return n
    if n < 2024: return f(n + 2) + n


print(f(2023) - f(2022))
