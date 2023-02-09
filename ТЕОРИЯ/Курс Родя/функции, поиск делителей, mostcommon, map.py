# функции
def f(x):
    return x ** 2


print(f(4))  # 4 ** 2 = 16

# поиск делителей числа
D = set()
{}  # массив без повторений (множество)
x = 10
for d in range(1, int(x ** 0.5) + 1):
    if x % d == 0:
        D.add(d)
        D.add(x // d)

# нахождение простого числа
def isPrime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x%d==0:
            return False
        return True
