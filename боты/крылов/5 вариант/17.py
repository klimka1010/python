f = open('17var02.txt')
a = [int(x) for x in f]
k = 0
mx = []
maxmx = 0
sum4is = 0
ss = []
ss1=[]

for i in range(len(a) - 1):
    if a[i] % 2 == 0:
        mx.append(a[i])
    ss = list(map(int, str(a[i])))
    ss1 = list(map(int, str(a[i+1])))
    sum4is = sum(ss) + sum(ss1)
    if sum4is == maxmx:
        k+=1

maxmx = max(mx)
print(k)
