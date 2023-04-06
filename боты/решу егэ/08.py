import itertools

k = 0
for i in itertools.product('12345', repeat=5):
    if i.count('1') == 3:
        k += 1

print(k)
