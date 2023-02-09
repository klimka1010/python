# функция
def f(x):
    return x ** 2

print(f(4))  # 4 ** 2 = 16


# поиск делителей числа
D = set()  # {} - массив без повторений (множество)
x = 10
for d in range(1, int(x ** 0.5) + 1):
    if x % d == 0:
        D.add(d)
        D.add(x // d)


# нахождение простого числа
def isPrime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
        return True

print(isPrime(7))   # True  (1)
print(isPrime(14))  # False (0)


# сколько раз встречаются символы // самое "простое" число
import collections

s = '12345'
print(collections.Counter(s).most_common())


# проверка массива на простые числа
a = [1, 2, 3, 4, 5]
b = list(map(isPrime, a))
print(b.count(True))


# дробление числа в массив
a = 1010
x = list(map(int, str(a)))
print(x)

print(sorted(x))
print(sorted(x, reverse=True))


