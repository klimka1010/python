import itertools

k = 0
for i in itertools.product('АЗЛОПЬ', repeat=6):
    k += 1
    if i.count('Ь') <= 1 and i.count('А') == 1 and i.count('З') <= 2:

        print(k, i)
