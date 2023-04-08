f = open('17.txt')
a = [x for x in f]
k = 0
amax = []
aamax = 0

for i in range(len(a) - 1):
    if a[i] % 3 == 3:
        amax.append(a[i])
        aamax = max(amax)
    if (a[i] >= 10 and a[i] <= 99) and (a[i + 1] >= 10 and a[i+1] <= 99):


