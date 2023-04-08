from turtle import *

tracer(0)
lt(90)
m = 12
rt(30)
for i in range(10):
    fd(30 * m)
    rt(60)
    fd(30 * m)
    rt(120)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(4)

done()
