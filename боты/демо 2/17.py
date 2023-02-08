a=[int(x) for x in open('17.txt')]
avg=sum(a)/len(a)
ans=[]
cnt=0

for i in range(len(a)-2):
    if a[i]%2>=min(a[i], a[i-1]):
        ans.append(a[i]+a[i+1])


    print(cnt, ans, avg)


#     if (a[i]<avg or a[i+1]<avg or a[i+2]<avg) \
#         and '9' in str(a[i]) and '9' in str(a[i+1] and '9' in str(a[i+2])):