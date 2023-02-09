# рекурсии

# нахождение факториала
def f(x):
    if x < 1:
        return 1
    else:
        return x * f(x - 1)
print(f(5))

# рекурсия на 16 задание // найти сколько путей есть из начала (х) до конца (end)
def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x * 2, end)
print(f(1,10))


# подключение кеша для быстрого подсчета длинной рекурсии
import functools
@functools.lru_cache(None)
def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x * 2, end)
print(f(1,499))


# try, except
a = [1, 2, 3, 4, 5]
try:
    print(a[10])
except:
    print('ошибка')