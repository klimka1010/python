from turtle import *
lt(90)
speed(1000)
pu()
# fd(100 * 3)
rt(90)
# fd(100 * 3)
rt(45)
pd()
for i in range(10):
    fd(30 * 7)
    rt(90)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*7, y*7)
        dot(2)
update()
done()
