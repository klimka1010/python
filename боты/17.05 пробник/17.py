f = open('17.txt')
a = [int(x) for x in f]
kol = 0
k = 0
el=[]
for i in range(len(a) - 1):
    if int(a[i]) % 3 == 0:
        kol += 1

for i in range(len(a) - 1):
    if (a[i] < 0 or a[i + 1] < 0) and (a[i] + a[i + 1]) < kol:
        k += 1
        el.append(a[i]+a[i+1])
print(k, max(el))
