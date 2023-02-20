f = open('27v01_A.txt')
data = []
q = 15
N, P = map(int, f.readline().split())
l = r = ms = s = 0

for i in range(N):
    a, b = map(int, f.readline().split())
    data += [[a, (b + q - 1) // q]]

for i in range(N):
    while r < N and data[r][0] - data[i][0] <= P:
        s += data[r][1]
        r += 1
    while data[i][0] - data[l][0] > P:
        s -= data[l][1]
        l += 1
    ms = max(ms, s)

print(ms)

# 1531  6362
