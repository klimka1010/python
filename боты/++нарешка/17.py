f = open('17_7619.txt')
a = [int(x) for x in f]
maxd=99
k=0
for i in range(len(a) - 1):
    if (len(str(a[i])) == 2 or len(str(a[i+1])) == 2):
        if (a[i] + a[i+1]) % 99 == 0:
            k+=1
            print(k, a[i]+a[i+1])

# and (a[i] + a[i+1] % 99) == 0










# for i in range(len(a) - 1):
#     if len(str(a[i])) == 2:
#         maxd.append(a[i])
# print(max(maxd))
