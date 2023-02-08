f=open('27-1a.txt')
N=int(f.readline())
s=0
abc=0
w=0
ss=10000
for i in range (N):
    a,b = map(int, f.readline().split())
    x=min(a,b)
    s+=x
    abc=abs(a-b)
    if abc % 3 > 0:
        w = min(abc, ss)
    # print(w)

if x % 3 != 0:
  print(x)
else:
  print(x, abc)
  print(x+abc)