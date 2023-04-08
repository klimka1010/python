f = open('17var09.txt')
a = [x for x in f]
k = 0

for i in range(len(a) - 1):
    if a[i] % 5 == 0:
        k += 1
print(a)
