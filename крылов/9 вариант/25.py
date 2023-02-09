# поиск делителей числа
D = set()  # {} - массив без повторений (множество)
a = [int(x) for x in range(850000, 1000000)]
for d in range(1, int(a[0] ** 0.5) + 1):
    if a[0] % d == 0:
        D.add(d)
        D.add(a[0] // d)
