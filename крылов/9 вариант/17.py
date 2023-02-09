f = open('17var09.txt')
a = [int(x) for x in f]
k = 0
s = []

for i in range(len(a) - 1):
    if (a[i] % 5 == 0 and a[i] % 2 != 0) and (a[i + 1] % 5 == 0 and a[i + 1] % 2 != 0):
        k += 1
        s.append(abs(a[i] - a[i + 1]))
print(k, max(s))
