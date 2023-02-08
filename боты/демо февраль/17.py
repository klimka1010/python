a=[int(x) for x in open('17.txt')]
avg=sum(a)/len(a)
ans=[]

for i in range(len(a)-2):
    if (a[i]<avg or a[i+1]<avg or a[i+2]<avg) \
        and '9' in str(a[i]) and '9' in str(a[i+1] and '9' in str(a[i+2])):
        ans.append(a[i]+a[i+1]+a[i+2])
    print(len(ans))
