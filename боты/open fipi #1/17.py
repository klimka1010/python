f = open('17_7089.txt')
a = [x for x in f]
mmin = 8
k = 0
minn = []

for i in range(len(a) - 1):
    if int(a[i]) % 111 == mmin or int(a[i+1]) % 111 == mmin:
        k += 1
        minn.append(a[i] + a[i+1])
print(k, min(minn))
