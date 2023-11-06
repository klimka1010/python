19-21







# from functools import lru_cache
# # import sys
# # sys.setrecursionlimit(10000)
# @lru_cache(None)
# def f(n):
#     if n<11: return n
#     if n>=11: return n+f(n-1)
#
# print(f(2024)-f(2021))
#
















# import sys
# import functools
# sys.setrecursionlimit(5000)
# @functools.lru_cache(None)
# def f(n):
#     if n<11: return 10
#     if n>=11: return n+f(n-1)*n
#
# print(f(2024)-f(2022))
#









# def f(n):
#     if n>=2025: return n
#     if n<2025: return n+f(n+2)
#
# print(f(2022)-f(2023))