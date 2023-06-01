import itertools

k = 1

for i in itertools.product('АЙКОС', repeat=5):
    a=''.join(i)
    if i.count('О') <= 1 and 'СС' not in i:
        k+=1
        print(k,i)

# 2990