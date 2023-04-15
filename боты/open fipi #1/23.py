def f(x, end):
    if x>end: return 0
    if x==end: return 1
    if x<end: return f(x+1, end) + f(x+2, end) + f(x*3, end)

print(f(4,10)*f(10,20)*f(21,22))

# 715, !1430, 1157,