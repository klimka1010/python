from turtle import *

tracer(0)
lt(90)
rt(315)
m = 20

for i in range(7):
    fd(16 * m)
    rt(45)
    fd(8 * m)
    rt(135)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(4)
done()
