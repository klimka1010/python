a =input()
b =input()
print(a,b)







# for y in range (34, 59+1):
#     def F(x, y, k):
#         if x>y:
#             return 0
#
#         if x==y:
#             if k == 6:
#                 return 1
#             else: return 0
#             k+=1
#
#         return F(x+1, y, k) + F(x+2, y, k) + F(x*2, y, k)
#
# print(F(1, 11, 6))
# 11


# def F(x, y):
#     if x > y: return 0
#     if x == 10: return 0
#     if x == 11: return 0
#     if x == y: return 1
#     else: return F(x+1, y) + F(x+2, y) + F(x*3, y)
# print(F(1, 8) * F(8, 28))


# def F(n):
#     if n == 0: return 0
#     if n % 3 == 0 and n > 0: return n + F(n - 3)
#     if n % 3 > 0: return n + F(n - (n % 3))
#
# print(F(26))


# def F(n):
#     if n == 0: return 0
#     elif n > 0 and n % 2 == 0: return F(n//2)
#     elif n % 2 != 0: return 1 + F(n-1)
#
# n = 0
#
# while True:
#     if F(n) == 11:
#         print(n)
#         break
#     n += 1



# def F(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return F(n-1) + 2 ** (n - 1) #! степень в скобке если сложная
#
# print(F(12))



# f = [1] * 3600
# for n in range (2,3600):
#     f[n] = (2*n - 1) * f*(n-1)
# print (f[3516] / f[3513])