from fnmatch import *

k = 0
for i in range(273, 10 ** 9, 273):
    s = str(i)
    if fnmatch(s, '12??46*1'):
        k += 1
print(k)
