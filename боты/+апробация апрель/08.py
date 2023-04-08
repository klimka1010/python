# import itertools
#
# k = 0
# for i in itertools.product('АВЛОР', repeat=4):
#     k += 1
#     print(k, i)
# 251

# import itertools
#
# k = 0
# for i in itertools.product('КЛМНО', repeat=4):
#     k += 1
#     print(k, i)
#
# # 51

import itertools

k = 0
for i in itertools.product('ВОРТА', repeat=6):
    k += 1
    print(k, i)

# 920