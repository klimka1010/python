from turtle import *

tracer(0)
lt(90)
m = 20

for i in range(4):
    fd(10 * m)
    rt(270)
pu()
fd(3*m)
rt(270)
fd(5*m)
rt(90)
pd()
for i in range(2):
    fd(10*m)
    rt(270)
    fd(12*m)
    rt(270)

pu()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m, y*m)
        dot(4)

done()
