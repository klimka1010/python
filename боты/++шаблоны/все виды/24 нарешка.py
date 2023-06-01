f = open('k7.txt').readline()
k = 0
m = 0

for i in range(len(f)-2):
    if f[i] == 'A' and f[i+1] == 'B' and f[i+2] == 'C':
        k+=1
        # if k>m:
        #     m=k
        # else:
        #     k=0

print(k)
