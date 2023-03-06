from itertools import *
import itertools
a = list(itertools.product('01234567', repeat=5))
count = 0
for x in a:
    for i in range(1):
        if x[i] == '4':
            count += 1
print(count)

# for x in a:
    # print(''.join(x))  # join(x) переводит кортеж (x) в строку
# print(a)  # список кортежей получаем