import re

for x in range(21,10**8,21):
    if re.fullmatch('1234.*54', str(x)) is not None:
        print(x, x//21)