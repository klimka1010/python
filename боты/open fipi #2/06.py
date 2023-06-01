from turtle import *
tracer(0)
lt(90)
m=20

for i in range(2):
    fd(10*m)
    rt(90)
    fd(18*m)
    rt(90)
pu()
back(6*m)
rt(90)
fd(9*m)
lt(90)
pd()
for i in range(2):
    fd(17*m)
    rt(90)
    fd(5*m)
    rt(90)

pu()
for x in range(-20,20):
    for y in range(-20, 20):
        goto (x*m, y*m)
        dot(4)



done()