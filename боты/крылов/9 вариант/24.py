# 15
f = open('24var09-13.txt').readline()
a = [x for x in f]
k = 0
m = 0

for i in range(0, len(f) - 2):
    while a[i] == 'X':
        k += 1
        if k > m:
            m = k
        else:
            k = 0
        break

for i in range(1, len(f) - 1):
    while a[i] == 'Y':
        k += 1
        if k > m:
            m = k
        else:
            k = 0
        break

for i in range(2, len(f)):
    while a[i] == 'Z':
        k += 1
        if k > m:
            m = k
        else:
            k = 0
        break

print(k)
