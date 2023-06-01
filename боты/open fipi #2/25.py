import re

for x in range(23, 10 ** 9, 23):
    if re.fullmatch('12345.7.8', str(x)) is not None:
        print(x, x // 23)
