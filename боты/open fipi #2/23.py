def f(x, end):
    if x<end: return 0
    if x==end: return 1
    if x>end: return f(x-1, end) + f(x//2, end)

print(f(30, 9)*f(9,1))