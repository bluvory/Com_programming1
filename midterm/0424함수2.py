# 프랙털 (recursion)
import turtle
def tree(length):
    if length > 35:
        t.forward(length)
        t.right(20)
        tree(length-15)
        t.left(40)
        tree(length-15)
        t.right(20)
        t.backward(length)

t = turtle.Turtle()
t.left(90)
t.color("green")
t.speed(0)
tree(90)
 

# 순환호출
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("factorial(5)=", factorial(5))


# 막대 그래프 그리기
import turtle

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))
    t.right(90)

    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

data = [120, 56, 309, 220, 156, 23, 98]
t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)
for d in data:
    drawBar(d)


# 터틀 메이즈 러너
def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

t = turtle.Turtle()
screen = turtle.Screen()
screen.onkey(turn_left, "Left")
screen.onkdy(turn_right, "Right")

import random
import turtle

def draw_maze(x, y):
    for i in range(2):
        t.penup()
        if i==2:
            t.goto(x+100, y+100)
        else:
            t.goto(x, y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

draw_maze(-300, 200)
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

t.penup()
t.goto(-300,250)
t.speed(1)
t.pendown()
screen.listen()  # 키보드 이벤트를 기다림
screen.mainloop()
