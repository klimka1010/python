def f(x,end):
    if x>end: return 0
    if x==end: return 1
    if x==11: return 0
    if x<end: return f(x+1,end) + f(x*2,end) + f(x*3, end)

print(f(2,15)*f(15,25))













# def f(x,end):
#     if x>end: return 0
#     if x==12: return 0
#     if x==end: return 1
#     if x<end: return f(x+1,end) + f(x+2,end) + f(x*2,end)
#
# print(f(2,9)*f(9,17))