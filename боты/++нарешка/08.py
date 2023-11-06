import itertools
k=0
for i in itertools.product('АКЛМНЯ', repeat=5):
    k+=1
    if i[0] == 'К' and i[1] == 'М':
        print(k, i)














# from itertools import *
# k=0
# for i in product('АВЛОР', repeat=4):
#     k+=1
#     if i[0] == 'Л':
#         print(k, i)