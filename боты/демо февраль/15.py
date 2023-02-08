def f(x):
    return (x%a==0) or ((x%23==0)<=(not(50<=x<=70)))

for a in range(1,100):
    if all(f(x)==1 for x in range(1,10000)):
        print(a)