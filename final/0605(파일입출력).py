# 11장 파일을 사용해봅시다

# 파일모드
# r:읽기모드 / w:쓰기모드 / a:추가모드 / r+:읽기와 쓰기모드
# open("파일경로.txt", "rt", encoding='UTF8')

infile = open("phones.txt", "r", encoding='UTF8')   # r:파일을 여는 모드
lines = infile.read()   #read(10) : 10글자만 읽어오기
print(lines)

infile = open("phones.txt", "r", encoding='UTF8')
for line in infile:
    print(line)
infile.close()


infile = open("phones.txt", "r", encoding='UTF8')
lines = infile.readlines()   # 줄단위로 읽되 다 읽어오기
print(lines)


# 한줄씩 읽기
infile = open("phones.txt", "r", encoding = 'UTF8')
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline().rstrip()   # 읽은값에 대해서 잘라버려라
infile.close()

infile = open("phones.txt", "r", encoding = 'UTF8')
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()


# 파일에 데이터 쓰기 : "w"
outfile = open("phones1.txt", "w",encoding = 'UTF8')
outfile.write("피카츄 010-1111-1111\n")
outfile.write("라이츄 010-2222-2222\n")
outfile.close()

import os.path
if os.path.isfile("phones1.txt"):
    print("동일한 이름의 파일이 이미 존재합니다")
else:
    outfile = open("phones1.txt", "w", encoding = 'UTF8')
    outfile.write("피카츄 010-1111-1111\n")
    outfile.write("라이츄 010-2222-2222\n")
    outfile.close()


# 파일에 데이터 추가하기 : "a"
outfile = open("phones1.txt", "a")
outfile.write("피카츄 010-1111-1111\n")
outfile.write("라이츄 010-2222-2222\n")
outfile.close()


# 파일에서 단어 읽기 : split() -> 공백을 기준으로 분리
infile = open("proverbs.txt", "r")
for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()


# Lab1 : 파일 복사하기
infilename = input("입력 파일 이름: ")
outfilename = input("출력 파일 이름: ")

infile = open(infilename, "r")
outfile = open(outfilename, "w")

s = infile.read()
outfile.write(s)

infile.close()
outfile.close()


# Lab2 : 행맨
import random

guesses = "
turns = 10
infile = open("words.txt", "r")
lines = infile.readlines()
word = random.choice(lines)

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end = "")
        else:
            print("_", end = "")
            failed += 1
        if failed == 0:
            print("사용자 승리")
            break
    print("")
    guess = input("단어를 추측하시오: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("틀렸음!")
        print(str(turns) + "기회가 남았음!")
        if turns == 0:
            print("사용자 패배 정답은 " + word)
infile.close()



# Lab3 : 숫자 데이터 저장하기
outfile = open("number.txt", "w")
for i in range(10):
    outfile.write(str(i) + " ")
# write로 저장할때는 문자데이터만 저장되기 때문에 수치데이터를 str을 통해 문자로 바꿔주기
outfile.close()


# with문 함께 사용하기
with open("with.txt", "w") as outfile:
    outfile.write("with블록을 사용하면 자동 닫힘")


# CSV 파일 읽기
infile = open("data.csv", "r")
for line in infile.readlines():
    line = line.strip()   #strip : 빈칸 모두 제거
    print(line)

    parts = line.split(",")

    for part in parts:
        print(" ", part)
infile.close()


# 이진 파일 다루기

# Lab : 이미지 파일 복사하기
filename1 = input("원본 파일 이름을 입력하시오: ")
filename2 = input("복사 파일 이름을 입력하시오: ")
infile = open(filename1, "rb")     # rb : read binary (이진으로 읽는다)
outfile = open(filename2, "wb")  # wb : write binary (이진으로 쓴다)
# 입력 파일에서 1024바이트씩 읽어서 출력 파일에 쓴다

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
oufile.close()
print(filename1 + "를 " + filename2 + "로 복사하였습니다. ")


# 임의 접근 파일
# 위치의 마지막 : EOF (end of file)
# 위치 표시자를 조작하는 함수 : seek(position)
# 현재 위치를 반환하는 함수 : tell()

infile = open("alphabet.txt", "r+")
str = infile.read(10)
print("읽은 문자열 : ", str)
print("읽은 문자열 : ", str)

position = infile.tell()    # 현재 위치 반환
print("현재 위치: ", position)

position = infile.seek(0)   # 파일의 맨 처음으로 간다

str = infile.read(1)
print("다시 읽은 문자열 : ", str)
infile.close()


# 객체 입출력 : pickle모율 dump(), load()
import pickle
# 게임에서 사용되는 딕셔너리
gameOption = { "sound":8,"VideoQuality":"HIGH","Money":10000,"WeaponLIst":["gun", "missile", "knife"] }
file = open("save.p", "wb")     # 이진 파일 오픈
pickle.dump(gameOption, file)   # 딕셔너리를 피클 파일에 저장
file.close()   # 파일을 닫는다


import pickle
file = open("save.p", "rb")    # 이진 파일 오픈
obj = pickle.load(open("save.p", "rb"))   # 피클 파일에 딕셔너리를 로딩
print(obj)


# 파일 대화 상자
from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
 
readFile = askopenfilename()
if readFile != None:
    infile = open(readFile, "r")
for line in infile.readlines():
    line = line.strip()
    print(line)
infile.close()


# Lab : 메모장
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def open():
    file = filedialog.askopenfile(parent=window, mode=‘r’, filetypes = (("text files","*.txt"),("all files","*.*")))
    if file != None:
        lines = file.read()
        text.insert('1.0', lines)
        file.close()

def save():
    file = filedialog.asksaveasfile(parent=window, mode=‘w’, filetypes = (("text files","*.txt"),("all files","*.*")))
    if file != None:
    lines = text.get('1.0', END+'-1c')
    file.write(lines)
    file.close()
    
def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
    window.destroy()
    
def about():
    label = messagebox.showinfo("About", "메모장 프로그램")

window = Tk()
text = Text(window, height=30, width=80)
text.pack()
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장하기", command=save)
filemenu.add_command(label="종료", command=exit)
helpmenu = Menu(menu)
menu.add_cascade(label="도움말", menu=helpmenu)
helpmenu.add_command(label="프로그램 정보", command=about)
window.mainloop()
