# переводы в системы счисления
x = 10
x2 = bin(x)[2:]
x8 = oct(x)[2:]
x16 = hex(x)[2:]
print(x, x2, x8, x16)

# перевод в двугую систему счисления
s = 5 ** 2019 - 5 ** 1019 + 25 ** 600 - 125
k = 0
t = ''

while s > 0:
    t += (str(s % 5))
    s = s // 5
print(t.count('4'))

# itertools
import itertools

a = list(itertools.product('ABC', repeat=2))  # перебор всевозможных (2) комбинаций из букв
print(a)

a = list(itertools.permutations('ABC', r=3))  # без повторений (уникальные вариации)
print(a)

# ###


# подсчет символов в числе
a = 187236458279240723484
print(str(a).count('3'))

# ###
