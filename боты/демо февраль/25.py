from fnmatch import *
for i in range(151, 10**9, 151):
    if fnmatch(str(i), '2?34?56?8'):
        print(i, i//151)


