score = int(input("성적을 입력하시오: "))

if score >= 60:
    print("합격입니다. ")
    print("축하합니다")
else:
    print("불합격입니다. ")
    print("아쉬워요")

print("수고했어요")


import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("거북이가 여기오면 양수")
t.goto(100, 0)
t.write("거북이가 여기오면 0")
t.goto(100, -100)
t.write("거북이가 여기오면 음수")

t.goto(0, 0)
t.pendown()
n = turtle.textinput("", "숫자를 입력하시오")
n = int(n)

if n > 0:
    t.goto(100, 100)
elif n == 0:
    t.goto(100, 0)
elif n < 0:
    t.goto(100, -100)
