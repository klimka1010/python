# переводы в системы счисления
x = 10
x2 = bin(x)[2:]
x8 = oct(x)[2:]
x16 = hex(x)[2:]
print(x, x2, x8, x16)

# ###


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
