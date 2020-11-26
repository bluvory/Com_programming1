import turtle
t = turtle.Turtle()
t.shape("turtle")

name = turtle.textinput("", "이름을 입력하시오")
t.write("안녕" + name)

for i in range(4):
    t.left(90)
    t.forward(100)
    t.write("안녕" + name)
