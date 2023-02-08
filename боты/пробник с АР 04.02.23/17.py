f=open('17.txt')
n=int(f.readline())
a=[int(f.readline()) for i in range(n)]
m12=-10000000
k=0
m=10000000

for i in range(len(a)):
    x = a[i]
    if abs(x)%100==12:
        m12=max(m12, x)

for i in range(len(a)-1):
    x,y = a[i], a[i+1]
    if abs(x)%100==12 or abs(y)%100==12:
        if (x+y)**2 < m12**2:
            k+=1
            m=min(m,x+y)

print(k,m)
