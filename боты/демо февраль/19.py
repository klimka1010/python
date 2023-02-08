def f(a,b,c,m):
    if a+b>=88: return c%2==m%2
    if c==m: return 0
    h=[f(a+1, b, c+1, m), f(a*3, b, c+1, m), f(a, b+1, c+1, m), f(a, b*3, c+1, m),]
    return any(h) if (c+1)%2==m%2 else any(h)

for s in range(1,81+1):
    for m in range(1,5):
        if f(6,s,0,m)==1:
            print(s,m)
            break