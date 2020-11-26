# 거북이 경주 게임 (p231)
import turtle
import random

screen = turtle.Screen()
img1 = "/rabbit.gif"
img2 = "/turtle.gif"
screen.addshape(img1)
screen.addshape(img2)

t1 = turtle.Turtle()
t1.shape(img1)
t1.pensize(5)
t1.penup()
t1.goto(-300, 0)

t2 = turtle.Turtle()
t2.shape(img2)
t2.pensize(5)
t2.penup()
t2.goto(-300, -200)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

for i in range(10):
    d1 = random.randint(1, 30)
    t1.forward(d1)
    d2 = random.randint(1, 30)
    t2.forward(d2)

totald1 = totald2 = 0
while True:
    d1 = random.randint(1, 30)
    t1.forward(d1)
    totald1 += d1
    d2 = random.randint(1, 30)
    t2.forward(d2)
    totald2 += d2
    
    if totald1 >= 300 or totald2 >=300:
        break

t1.write(totald1)
t2.write(totald2)

# 애니메이션 만들기
import turtle
t = turtle.Turtle()
t.reset()

radius = 200

def draw_shape(radius, color1):
    radius = 200
    t.left(270)
    t.width(3)
    t.color("black", color1)
    t.begin_fill()
    t.circle(radius / 2.0, -180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius / 2.0, -180)
    t.end_fill()

draw_shape(radius, "red")
t.setheading(180)
draw_shape(radius, "blue")

# 에스터로이드 게임

# 앵그리 터틀 게임

# 암호화와 복호화 (ord : 문자->숫자, chr : 숫자->문자)
plain_text = "Love will find a way."
print("원문:", plain_text)

for ch in plain_text:
    x = ord(ch)
    x += 5
    changed_ch = chr(x)
    encrypted_text = encrypted_text + changed_ch

print("암호문:", encrypted_text)

plain_text = ""
for ch in plain_text:
    x = ord(ch)
    x -= 5
    changed_ch = chr(x)
    plain_text = plain_text + changed_ch

print("원문:", plain_text)

# 크리스마스 트리 만들기


