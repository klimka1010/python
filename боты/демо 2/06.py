from turtle import *

tracer(0)
lt(90)

for i in range (10):
    fd(30*15)
    lt(120)

up()
for x in range (-15,15):
    for y in range(-15,15):
        goto(x*15,y*15)
        dot(4)


update()
done()
