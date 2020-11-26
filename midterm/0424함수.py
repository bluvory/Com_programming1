# 면적 구하기
def square(a):
    area = a*a
    return area

def triangle(a, h):
    area = a*h/2
    return triangle

length = int(input("사각형 한 변의 길이를 입력하시오"))
print("사각형의 면적은", square(length), "이다")
print("-"*20)

w = int(input("삼각형의 밑변의 길이를 입력하시오"))
h = int(input("삼각형의 높이의 길이를 입력하시오"))
print("삼각형의 면적은 ", triangle(w, h), "이다")


# 다각형 그리기
def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n):
    for x in rnage(n):
        t.forward(a)
        t.left(360/n)
    

# 클릭하는 곳에 사각형 그리기
import turtle
t = turtle.Turtle()

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()   # 색깔 칠해주기
    t.color("green")
    square(50)
    t.end_fill()  # 채우기 멈추기

s = turtle.Screen()  # 그림이 그려지는 화면을 얻는다
s.onscreenclick(drawit)  # 마우스 클릭 이벤트 처리 함수를 등록한다


# 마우스로 그림 그리기
import turtle

def draw(x, y):
    t.goto(x, y)

t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)
s = turtle.Screen()
s.onscreenclick(draw)


# 마우스로 그림 그리기2
import turtle

def draw(x, y):
    t.goto(x, y)

t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)

s = turtle.Screen()
s.onscreenclick(draw)   # 마우스 클릭 이벤트 처리 함수를 등

s.onkey(t.penup, "Up")   # 키보드 이벤트 처리 함수를 등록
s.onkey(t.pendown, "Down")   # 키보드 이벤트 처리 함수를 등록
s.listen()   # 키보드 이벤트를 기다린다



# 방향키에 따라 거북이 이동하기
# t.setheading() : 거북이 방향 설정

import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()
    
t.shape("turtle")
t.speed(0)
s = turtle.Screen()
t.onkey(turn_right, "Right")
t.onkey(turn_up, "Up")
t.onkey(turn_left, "Left")
t.onkey(turn_down, "Down")
t.onkey(blank, "Escape")
t.listen()   # 키보드 입력을 기다림


# 영어단어 맞추기
import time
import random

def word(q):
    score= 0
    for x in range(q):
        i = random.randint(0, 9)
        print("**문제번호:", x+1)
        print(words_kor[i])
        answer = input("답:")
        if word[i] == answer:
            print("통과")
            score += 20
        else:
            print("다시")
            score -= 10
        print("_"*20)
        print()
    return score

words = ["pen", "book", "ruler", "pencil", "notebook", "eraser", "clock", "glue", "blackboard", "chair"]
words_kor = ["볼펜", "책", "자", "연필", "노트", "지우개", "시계", "풀", "칠판", "의자"]

print("-"*30)
print("#한글 단어에 적합한 영어 단어를 쓰시오")
print("-"*30)
q = int(input("문제 수를 입력하시오"))
print("enter키를 누르면 시작합니다")
input()

start = time.time()

print("점수는", word(q), "입니다")
end = time.time()
diff = end - start
diff = format(diff, ".2f")   # 소숫점 두째자리까지 나타내기
print("걸린 시간은", diff, "초입니다.")





