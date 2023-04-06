def f(x, y, A):
    return ((x < 6) <= (x ** 2 < A)) and ((y ** 2 <= A) <= (y <= 6))


print(min(A for A in range(1, 300) if all(f(x, y, A) for x in range(0, 300) for y in range(0, 300))))

#
# count = 0
# for a in range(1, 300):
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6)):
#                 k += 1
#     if k == 90_000:
#         count += 1
# print(count)
