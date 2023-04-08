from fnmatch import *

for i in range(219, 10 ** 7, 219):
    if fnmatch(str(i), '2?1*56'):
        print(i, i // 219)
