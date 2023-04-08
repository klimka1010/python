import functools


@functools.lru_cache(None)
def f(i):
    if a[i][2] == 0:
        return a[i][1]
    else:
        return a[i][1] + max(f(k - 1) for k in a[i][2:])


a = []

for line in open('22.txt'):
    a.append(list(map(int, line.replace(';', ' ').split())))

print(max(f(i) for i in range(len(a))))
