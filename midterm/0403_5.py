# 10번대 확인

no = int(input("Enter a number"))

if no >= 10 and no < 20:
    print("10번대 이구나")
else:
    print("10번대가 아니다")


# 윤년 계산기

year = int(input("년도를 입력하시오"))

#400으로 나누어 떨어지면 윤년
#4로 나누어 떨어지고 100으로 나누어 떨어지지 않는 해

if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    day = 366
    print(year, "는 윤년이다")
else:
    day = 365
    print(year, "는 평년이다")

print("%d 해는 일년이 %d 날이다" %(year, day))


# 동전던지기
import random
print("동전을 던지기 게임시작")
coin = random.randrange(2)

if coin == 0:
    print("앞면")
else:
    print("뒷면")

print("게임이 종료되었다.")


# 동전던지기2
import random
print("동전을 던지기 게임시작")
coin = random.randrange(2)

if coin:
    print("뒷면")
else:
    print("앞면")

print("게임이 종료되었다.")


# 거북이놀이

import turtle

# 거북이를 만든다
t = turtle.Turtle()
# 거북이가 그리는 선의 두께를 3으로 한다
t.width(3)
# 커서의 모양을 거북이로 한다
t.shape("turtle")
# 거북이를 3배 확대한다
t.shapesize(3, 3)

# 무한루프이다
while True:
    command = input("명령을 입력하시오: ")
    if command == "l":
        t.left(90)
        t.forward(100)
    if command == "r":
        t.right(90)
        t.forward(100)
