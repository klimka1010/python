import re

for x in range(23, 10 ** 9, 23):
    if re.fullmatch('2.*5443.1', str(x)) is not None:
        print(x, x // 23)

# 2*5443?1
