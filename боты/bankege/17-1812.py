f = open('17-1812.txt')
a = [int(x) for x in f]
k = 0
m = []
minEl = []
mmin = 0

for i in range(1, len(a) - 1):
    if a[i] % 23 == 0:
        minEl.append(a[i])
        mmin = min(minEl)

    if abs(a[i]) % mmin == 0 or abs(a[i + 1]) % mmin == 0:
        k += 1

        m.append(max(a[i] % minEl == 0 + a[i + 1] % minEl == 0))
print(k)
