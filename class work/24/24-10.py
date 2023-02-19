f=open('k7-97.txt')
N=f.readline()
k=0
m=0


for i in (N):
    if f[i] == 'C':
        k+=1

        if k>m:
            m=k
    else:
        k=0

print(m)
