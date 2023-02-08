from turtle import *

import turtle

# Основные цвета для персонажа
BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'

# Главный объект
t = turtle.Turtle()
def j():
    t.pu()
    t.pensize(10)
    t.speed(1)
    t.color("red")
    t.left(180)
    t.forward(300)
    t.left(90)
    t.forward(250)
    t.pd()
    t.left(180)
    t.right(30)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.pu()
    t.left(60)
    t.forward(50)
    t.pd()
    for i in range(12):
        t.left(30)
        t.forward(20)
    t.pu()
    t.forward(50)
    t.left(30)
    t.pd()
    t.forward(100)
    t.back(50)
    t.left(120)
    t.back(50)
    t.forward(100)









# Метод для рисования тела
def body():
	t.pensize(10) # Размер кисти

	t.fillcolor(BODY_COLOR) # Цвет заполнения
	t.begin_fill()

	# Сторона справа
	t.right(90)
	t.forward(50)
	t.right(180)
	t.circle(40, -180)
	t.right(180)
	t.forward(200)

	# Голова
	t.right(180)
	t.circle(100, -180)

	# Сторона слева
	t.backward(20)
	t.left(15)
	t.circle(500, -20)
	t.backward(20)

	t.circle(40, -180)
	t.left(7)
	t.backward(50)

	t.up()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.down()

	t.right(240)
	t.circle(50, -70)

	t.end_fill()


# Рисуем очки
def glass():
	# Передвигаем черепашку
	t.up()
	t.right(230)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.right(90)
	t.down()

	# Устанавливаем цвет
	t.fillcolor(GLASS_COLOR)
	t.begin_fill()

	t.right(150)
	t.circle(90, -55)

	t.right(180)
	t.forward(1)
	t.right(180)
	t.circle(10, -65)
	t.right(180)
	t.forward(110)
	t.right(180)

	t.circle(50, -190)
	t.right(170)
	t.forward(80)

	t.right(180)
	t.circle(45, -30)

	t.end_fill()


# Рисуем рюкзак
def backpack():
	t.up()
	t.right(60)
	t.forward(100)
	t.right(90)
	t.forward(75)

	t.fillcolor(GLASS_COLOR)
	t.begin_fill()

	t.down()
	t.forward(30)
	t.right(255)

	t.circle(300, -30)
	t.right(260)
	t.forward(30)
	t.end_fill()


# Вызываем все необходимые методы
j()

turtle.done()




# for i in range (100):
#     pu()
#     speed(1)
#     color("red")
#     left(180)
#     forward(300)
#     left(90)
#     forward(250)
#     pd()
#     left(120)
#     forward(100)
#     right(45)
#     forward(100)
#     right(45)
#     forward(100)
#     back(100)
#     back(100)
#     left(45)
#     forward(100)
#     right(45)
#     back(100)
#     forward(100)
#



# pu()
#
# # for x in range(11):
# #     for y in range(11):
# #         goto(x*30,y*30)
# #         dot(10)
#
#
# done()