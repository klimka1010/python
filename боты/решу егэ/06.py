from turtle import *

tracer(0)
lt(90)
m = 30

for i in range(7):
    fd(10 * m)
    rt(120)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(4)


update()
done()