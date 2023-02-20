f = open('27v01_A.txt')
n, m = map(int, f.readline().split())
a = []
k = 15
l = r = ms = s = 0

for i in range(n):
    x, y = map(int, f.readline().split())
    a += [[x, (y + k - 1) // k]]

for i in range(n):
    while r < n and a[r][0] - a[i][0] <= m:
        s += a[r][1]
        r += 1
    while a[i][0] - a[l][0] > m:
        s -= a[l][1]
        l += 1
    ms = max(ms, s)
print(ms)
