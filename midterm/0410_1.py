import turtle  # 터틀 그래픽 모듈을 불러온다
import random  # 난수 모듈을 불러온다

screen = turtle.screen()
image1 = "./front.gif"
image2 = "./back.gif"

screen.addshape(image1)  # 이미지 추가
screen.addshape(image2)  # 이미지 추가

t1 = turtle.Turtle()   # 첫번째 거북이 생성

coin = random.randint(0, 1)

print("나온 값: ", coin)

if coin == 0:
    t1.shape(image1)   #거북이 모양 설정
    t1.stamp()
else :
    tl.shape(image2)
    t1.stamp()

    
# image1 = "./images/front.gif"  -> images폴더안 (폴더명 제대로 쓰기)
# image2 = "./images/back.gif"
