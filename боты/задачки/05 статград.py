def su(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
        return s


a1 = 123456789
a2 = 1987654321
#
for n in range(248456780, 250 * 10 ** 6):
    newn = n
    newn = newn * 2 + su(newn) % 2
    newn = newn * 2 + su(newn) % 2
    newn = newn * 2 + su(newn) % 2
    if newn >= a1 and newn <= a2:
        print(n, newn)
