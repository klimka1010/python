from turtle import *

tracer(0)
lt(90)
m = 35

for i in range(2):
    fd(7*m)
    rt(90)
    fd(18*m)
    rt(90)

pu()

fd(2*m)
rt(90)
fd(9*m)
lt(90)
pd()
for i in range(2):
    fd(8*m)
    rt(90)
    fd(5*m)
    rt(90)

pu()
for x in range(-35,35):
    for y in range(-35, 35):
        goto(x*m, y*m)
        dot(4)

done()