# 모듈 활용 기억력테스트

from turtle import*
from random import randint
from time import sleep

numbers = []

qno = int(textinput("", "몇 개의 숫자를 기억하시겠습니까? "))
if qno>1:
    setup(300, 200)

for i in range(qno):
    reset()   # 화면 지우고 거북위치 (0,0)
    ht()      # 거북이 모양 감추기
    pu()      # 펜을 들어 그림 안그려지게 하기
    goto(-30, 0)    # 거북이 위치 이동

    numbers.append(randint(1, 99))
    write(numbers[i], font=("", 32))
    sleep(2)    # 2초간 정지

success = True
for i in range(qno):
    unumber = int(input(str(i+1) + "번째 숫자 >> "))
    if unumber != numbers[i]:
        print(numbers, "오답입니다")
        success = False
        break
    if i == qno-1:
        print(numbers, "정답입니다")


# 모듈 활용 기억력테스트2

from turtle import*
from time import sleep
import random

wordlist = []
for i in range(65,123):
    if i<=90 or 97<=i:
        wordlist.append(chr(i))

words =[]

qno = int(textinput("", "몇 개의 알파벳을 기억하시겠습니까? "))
if qno>1:
    setup(300, 200)

for i in range(qno):
    reset()   # 화면 지우고 거북위치 (0,0)
    ht()      # 거북이 모양 감추기
    pu()      # 펜을 들어 그림 안그려지게 하기
    goto(-30, 0)    # 거북이 위치 이동

    words.append(random.choice(wordlist))                
    write(words[i], font=("", 32))
    sleep(2)    # 2초간 정지

success = True
for i in range(qno):
    uword = input(str(i+1) + "번째 알파벳 >> ")
    if uword != words[i]:
        print(words, "오답입니다")
        success = False
        break
    if i == qno-1:
        print(words, "정답입니다")


