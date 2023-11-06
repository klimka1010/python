# перевод в троичную!
def tr(n):
    s=''
    while n>0:
        s = str(n%3) + s
        n//=3
    return s


# for N in range (1,100):
#     n=bin(N)[2:]
#     n=str(n)
#     if N%3==0:
#         n=n+str(int(n)%10)
#     if N%3!=0:
#         s=N%3
#         s*=3
#         n=n+bin(s)[2:]
#
#     r=int(n,2)
#     if r>76:
#         print(N)

















# for N in range(202):
#     n=bin(N)[2:]
#     n=str(n)
#     if n.count('1') % 2 == 0:
#         n = '1'+n[:-2]+'10'
#     else:
#         n = '10'+n[2:]+'1'
#
#     r = int(n,2)
#     if r>202:
#         print(N)
#         break

