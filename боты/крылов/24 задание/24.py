# 15

f = open('24var09-13.txt')
a = f.readline()
k = 0
m = 0

# and a[i + 1] == 'Y' and a[i + 2] == 'Z'

c = list(map(str, str(a)))
for i in range(len(a) - 1):
    if a[i] == 'X' and a[i + 1] == 'Y' and a[i + 2] == 'Z':
        k += 1
        if k > m:
            m = k
        else:
            k = 0
print(k, m)
