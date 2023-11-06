from turtle import *

lt(90)
tracer(0)
m=20

for i in range(10):
    lt(90)
    fd(10*m)
    lt(90)
    fd(10 * m)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(4)

done()