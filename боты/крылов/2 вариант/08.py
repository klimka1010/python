from itertools import *

k = 0

for x in product('0123', repeat=5):
    if x.count('3') == 1 and x[0] != '0' and '03' not in ''.join(x) and '30' not in ''.join(x):
        k+=1
print(k)