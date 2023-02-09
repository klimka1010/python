f = open('17-1811.txt')
a = [int(x) for x in f]
k = 0
m = []

for i in range(len(a) - 1):
    maxx = max(a)
    if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and (a[i] + a[i + 1] <= maxx):
        k += 1
        m.append(a[i] + a[i + 1])
print(k, max(m))

# 2439 998
