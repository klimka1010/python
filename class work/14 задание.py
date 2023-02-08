def calc(x, a, b):
    x = int(str(x), a)
    s = ''
    while x>0:
        s+= str(x%b)
        x //= b
    return s[::-1]

for x in range (3, 30):
    if int('121', x) + int('1', 10) == int ('101', 7):
        if x % 3 == 0:
            print(calc(x, 10, 3))
















# for i in range(1, 30):
#     if int('60', 8) + i == int('120', 7):
#         y = i
#
# number = ''
# while y > 0:
#     number = str(y%6) + number
#     y //= 6
# print(number)


# for i in range(2, 30):
#     if int('101', i) + 13 == int('101', i+1):
#         print(i)


# for i in range(5, 30):
#     if int('12', i) * int('31', i) == int('402', i):
#         print(i)


# def prost(i):
#     for d in range (2, i):
#         if i % d == 0:
#             return False
#     return True
#
# s1=0
# for n in range (2, 10+1):
#     x = 437
#     summa = 0
#     while x > 0:
#         summa += x % n
#         x //= n
#     if prost(summa):
#         s1 += n
# print (s1)


# sum = 0
# for n in range (2, 10+1):
#     x = 804
#     number = ''
#     while x > 0:
#         number += str(x % n)
#         x //= n
#     if '1' in number:
#         sum += n
# print (sum)


# for n in range (3, 100):
#     x = 87
#     k = 0
#     while x > 0:
#         k += 1
#         x //= n
#
#     if k >= 3 and 87 % n == 2:
#         print(n)
#         break


# x = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
# s = set()    # создание множества
# while x > 0:
#     s.add (x % 16)
#     x //= 16
# print(len(s))


# x = 26 ** 2 + 169 - 11
# k = 0
# while x > 0:
#     if x % 13 == 12 or x % 13 == 2:
#         k += 1
#     x //= 13
# print (k)


# x = 5 * 216 ** 1256 - 5 * 36 ** 1146 + 4 * 6 ** 1053 - 1087
# k = 0
# while x > 0:
#     k += x % 6
#     x //= 6
# print(k)


# x = 81 ** 2017 + 9 ** 5223 - 81
# k = 0
# while x > 0:
#     if x % 9 == 8:
#         k+=1
#     x //= 9
# print(k)


# print (bin(4 ** 512 + 8 ** 512 - 2 ** 128 - 250).count('1'))
# print (bin(4 ** 512 + 8 ** 512 - 2 ** 128 - 250).count('0') - 1)


#bin - двоичная
#hex - шеснадцатиричная


# РОДЯ
#
# def calc(x, a, b):
# #     x = int(str(x), a)
# #     s = ''
# #     while x>0:
# #         s+= str(x%b)
# #         x //= b
# #     return s[::-1]
# #
# # x = 81 ** 2017 + 9 ** 5223 - 81
# # x = calc (x, 10, 2)
# # print(x.count('8'))