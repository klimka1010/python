s = 9 ** 18 + 3 ** 54 - 9
t = ''

while s > 0:
    t+=(str(s%3))
    s=s//3
print(t.count('2'))
