import itertools

k = 0
for i in itertools.product('АМОТ', repeat=4):
    k += 1
    if i[0] == 'О':
        print(k, i)
