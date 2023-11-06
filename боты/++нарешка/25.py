import re

for x in range(62961,10**9,62961):
    if re.fullmatch('.*31.*65.', str(x)) is not None:
        print(x,x//2031)

1 - 124















# import re
# for x in range(253, 10**8, 253):
#     if re.fullmatch('12..15.*6', str(x)) is not None:
#         print(x, x//253)