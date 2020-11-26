# 스파이럴
import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)  # 최고속도, 1:가장느린속도, 10의 빠른 속도
t.width(3)
length = 10  # 초기 선의 길이는 10으로 한다
t.pencolor(colors[length%6])  # 선 색상 변경

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5


# 사용자가 입력하는 숫자의 합 계산하기
while answer == "yes":
    number = int(input("숫자를 입력하시오: "))
    total += number
    answer = input("계속? (yes/no):")
    

# 숫자 맞추기 게임
while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tries += 1
    if guess < answer:
        print("낮음!")
    elif guess > answer:
        print("높음!")


# 초등학생을 위한 산수 문제 발생기
import random

correct = 0
wrong = 0

while True:
    x = random.randint(1,100)
    y = random.randint(1,100)

    print(x, "+", y, "=", end=" ")
    answer = int(input())
    
    if answer == x+y:
        print("잘했어요!!")
        correct += 1
    else:
        print("다음번에는 잘할 수 있죠?")
        wrong += 1
    if correct == 5:
        break


# 초등학생을 위한 산수 문제 발생기2
for i in range(3):
    correct = 0
    wrong = 0
    print("이름을 입력하시오:", end=" ")
    name = input()
    print()

    for cnt in range(5):
        x = random.randint(0,9)
        y = random.randint(0,9)

        if x < y:
        t = x
        x = y
        y = t

        print(x, "-", y, "=", end=" ")
        answer = int(input())
        
        if answer == x - y:
            correct += 1
        else:
            wrong += 1

    print("맞은 문제 수:", correct)
    print("틀린 문제 수:", wrong)
    students.append(name)
    scores.append(correct*20)
    print("-"*20)
    print()

for i in range(3):
    print(students[i], ":", end = " ")
    cnt = scores[i] // 20

    for value in range(cnt):
        print("*", end = " ")





# 모든 샌드위치 종류 출력하기
breads = ["호밀빵", "위트", "화이트"]
meats = ["마트볼", "쏘시지", "닭가슴살"]
vegis = ["양상추", "토마토", "오이"]
sauces = ["마요네즈", "허니 머스타드", "칠리"]

for b in breads:
    for m in meats:
        for v in vegis:
            for s in sauces:
                print(b+"+"+m+"+"+v+"+"+s)


# 시계 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.stamp()

move = 30
for i in range(12):
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(15)
    t.stamp()
    t.home()
    t.right(move)
    move += 30


# 점치는 게임
while True:
    name = input("이름:(종료하려면 엔터키)")

    if name == "":
        sys.exit()

    question = input("무엇에 대하여 알고 싶은가요?")
    print(name + "님", "\"", question, "\"에 대하여 질문주셨군요.")
    print("운명의 주사위를 굴려볼께요...")

    answers = random.randint(1,8)

    if answer == 1:
        print("네, 확실합니다.")

    elif answer == 2:
        print("전망이 좋을 거 같은데요.")

    elif answers == 3:
        print("믿으셔도 됩니다.")

    elif answers == 4:
        print("글쎄요 아닌 거 같군요.")


