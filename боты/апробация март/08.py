import itertools

a = list(itertools.product('АЙКОС', repeat=5))

for i in range(len(a)):
    a[i] = ''.join(a[i])
    if a[i].count('О') <= 1 and 'СС' not in a[i]:
        print(i + 1)
