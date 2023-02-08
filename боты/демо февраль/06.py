from turtle import *

tracer(0)
lt(90)

for i in range (6):
    fd(5*30)
    rt(60)

fd(5*30)
rt(90)

for i in range (2):
    fd(15*30)
    rt(90)
    fd(5*30)
    rt(90)

up()
for x in range (-30,30):
    for y in range(-30,30):
        goto(x*30,y*30)
        dot(4)


update()
done()
