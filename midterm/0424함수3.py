#
import turtle

def draw(x, y):
    t.goto(x, y)
    
t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)

s = turtle.Screen()
s.onscreenclick(draw)

s.onkey(t.penup, "Up")
s.onkey(t.pendown, "Down")

s.listen()


#
import turtle
t = turtle.Turtle()

t.shape("turtle")
t.speed(0)
t.pensize(2)
t.color("red")
t.hideturtle()
t.onscreenclick(t.goto)


#
import turtle
t= turtle.Turtle()

def turn_right():
    t.setheading
