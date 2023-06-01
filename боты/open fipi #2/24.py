f=open('24_7272.txt').readline()
k=0
m=0
f=f.replace('AB', '1').replace('CB', '1')
# for i in range(len(f)-1):
#     if f[i] == '1' or f[i+1] == '2' or f[i] == '2' or f[i+1] == '1':
#         k+=1
#         if k>m:
#             m=k
#             k=0
print(f.count('1'))