from turtle import *

tracer(0)
lt(90)
pd()
for i in range(5):
    fd(7*30)
    rt(90)
    fd(4*30)
    rt(90)
pu()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*30,y*30)
        dot(4)
update()
done()
