from itertools import *
import itertools

itertools.product()  # буквы могут повторяться
# repeat = 5
itertools.permutations()  # без повторения букв
# r = 5


# первая задача
a = list(itertools.product('ABCX', repeat=5))
count = 0
for x in a:
    if x.count('X') == 1:
        count += 1
print(count)
for x in a:
    print(''.join(x))  # join(x) переводит кортеж (x) в строку
print(a)  # список кортежей получаем


# вторая задача
a = list(itertools.product('АКРУ', repeat=5))
count = 0
for x in a:
    x = ''.join(x)  # join(x) переводит кортеж (x) в строку
    for counter in range(1):
        count+=1
        print(x, count)
# КККУК
# родя
a  = list(itertools.product('АКРУ', repeat = 5))
print(a[349])


#третья задача
4 светящихся элементов по три цвета == 3**4 == 81

# четвертая задача
a = list(itertools.product('+-', repeat=5))
print(len(a))

# пятая задача
a = list(itertools.product('ABCDX', repeat=4))
count = 0
for x in a:
    if x[0] == 'X' and x.count('X') == 1 or x.count('X') == 0:  # or x not in x
        count += 1
        print(x)  # дебажим код
print(count)


# шестая задача тупой перебор цветов
a = list(itertools.product('1234', repeat=4))
print(len(a))  # 4**4 == 2**8 == 256


# седьмая задача
a = list(itertools.product('ТИМОФЕЙ', repeat=5))
count = 0
for x in a:
    if x.count('Т') >= 1 and x.count('Й') <= 1:
        count += 1
print(count)

# восьмая задача переставляя буквы это permutations()
a = list(itertools.permutations('ЗАПИСЬ', r=6))  # r == длина слова
count = 0
# a = set(a)  # убирает все повторения
for x in a:
    f = ['АЬ', 'ИЬ']  # исключения
    if x[0] != 'Ь':
        s = ''.join(x)
        for forbidden in f:
            if forbidden in s:
                break
        else:
            count += 1

print(count)
