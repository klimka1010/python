f=open('24var09-13.txt')
a=f.readline()
k=0
ans=0
mass = a.split('Z')

for i in mass:
    if len(i) > ans:
        ans=len(i)
print(ans)



#
# for i in range(len(a)):
#     while 'Z' in a:
#         if 'Z' in a:
#             a=a.replace('Z', ' ', 1)
#     q=list(map(str, a.split()))
#     if (max(q, key=len)).isalpha():
#         k+=1
# print(k)