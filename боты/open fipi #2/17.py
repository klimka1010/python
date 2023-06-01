f = open('17_7267.txt')
a = [int(x) for x in f]
n = 8
k = 0
mmax = []

for i in range(len(a) - 1):
    if (a[i] % 117 == 8 or a[i + 1] % 117 == 8):
        mmax.append(a[i] + a[i + 1])
        k += 1

print(k, max(mmax))