from turtle import *

tracer(0)
lt(90)

for i in range(4):
    fd(10*20)
    rt(90)
    fd(20*20)
    rt(90)

pu()

fd(7*20)
rt(90)
fd(3*20)
lt(90)

pd()

for i in range (2):
    fd(70*20)
    rt(90)
    fd(80*10)
    rt(90)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*20, y*20)
        dot(4)
update()
done()