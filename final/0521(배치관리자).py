# 배치관리자 :  컨테이너 안에 존재하는 위젯의 크기와 위치를 자동적으로 관리하는 객체
# 배치관리자 종류 : pack grid place

from tkinter import*
window = Tk()
b1 = Button(window, text = "첫번째 버튼")
b2 = Button(window, text = "두번째 버튼")
b1.pack()
b2.pack()
window.mainloop()


# 수평으로 정렬하는 법 : side = LEFT, RIGHT
from tkinter import*
window = Tk()
b1 = Button(window, text = "첫번째 버튼")
b2 = Button(window, text = "두번째 버튼")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
window.mainloop()


# 버튼 세개
from tkinter import*
window=Tk()
btnList = [""]*3
for i in range(0, 3):
    btnList[i] = Button(window, text="버튼"+str(i+1))
for btn in btnList:
    btn.pack(side = RIGHT)
window.mainloop()


# 수직으로 정렬하는 방법 : side = TOP, BOTTOM
from tkinter import*
window = Tk()
btnList = [""]*3
for i in range(0, 3):
    btnList[i] = Button(window, text="버튼"+str(i+1))
for btn in btnList:
    btn.pack(side = TOP)
window.mainloop()


# 위젯 사이에 여백을 주는 방법 : padx = 픽셀값(위젯과 위젯사이의 거리), pady = 픽셀값
from tkinter import*
window = Tk()
b1 = button(window, text = "첫번째 버튼")
b2 = button(window, text = "두번째 버튼")
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)
window.mainloop()


# 위젯 내부에 여백을 주는 방법 : ipadx= 픽셀값(위젯 내부의 거리), ipady = 픽셀값
from tkinter import*
window = Tk()
b1 = button(window, text = "첫번째 버튼")
b2 = button(window, text = "두번째 버튼")
b1.pack(side = LEFT, ipadx = 10)
b2.pack(side = LEFT, ipadx = 10)
window.mainloop()


# 격자 배치 관리자 grid (row=행번호, column=열번호)
from tkinter import*
window = Tk()
l1 = Label(window, text = "화씨")
l2 = Label(window, text = "섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨")
b2 = Button(window, text="섭씨->화씨")
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


# 버튼 이벤트 처리
from tkinter import*
def process():
    print("안녕하세요?")
window = Tk()
button = Button(window, text="클릭하세요!", command=process)
button.pack()
window.mainloop()


# 버튼 이벤트 처리
from tkinter import*
def process():
    temperature = float(e1.get())
    mytemp = (temperature - 32)*59
    e2.insert(0, str(mytemp))
# insert : 화면안에 집어넣기

window = Tk()
l1 = Label(window, text = "화씨")
l2 = Label(window, text = "섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨", command=process)
b2 = Button(window, text="섭씨->화씨")
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


# 절대 위치 배치 관리자 place
from tkinter import*
window = Tk()
w = Label(window, text = "박스 #1", bg = "red", fg = "white")
w.place(x=0, y=0)
w = Label(window, text = "박스 #2", bg = "green", fg = "balck")
w.place(x=20, y=20)
w = Label(window, text = "박스 #3", bg = "blue", fg = "white")
w.place(x=40, y=40)
window.mainloop()


# 이미지 표시 프로그램
from tkinter import*
def change_img():
    path = inputBox.get()
    img = PhotoImage(file = path)
    imageLabel.configure(image = img)
    imageLabel.image = img
window = Tk()
photo = PhotoImage(file = "wl.gif")
imageLabel = Label(window, image = photo)
imageLabel.pack()
inputBox = Entry(window)
inputBox.pack()
button = Button(windwo, text = 'Submit', command = change_img)
button.pack()
window.mainloop()


#
from tkinter import*
btnList = [""]*9
fnameList = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]
photoList = [None]*9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0
window = Tk()
window.geometry("600x600")
for i in range(0, 9):
    photoList[i] = PhotoImage(file = "images/" + fnameList[i])
    btnList[i] = Button(window, image = PhotoList[i])
for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 200
    xPos = 0
    yPos += 200
window.mainloop()


# 계산기 프로그램1
# 사용자 인터페이스 작성 : 격자 배치 관리자, 버튼 위젯, 엔트리 위젯
# 계산기 프로그램2
from tkinter import*
window = Tk()
window.title("My Calculator")
display = Entry(window, width = 33, bg = "yellow")
display.grid(row=0, column = 0, columnspan=5)

# 계산기 프로그램3
button_list = ['7', '8', '9', '/', 'C', '4', '5', '6', '*', ' ', '1', '', '3', '-', ' ', '0', '.', '=', '+', ' ']
row_index = 1
col_index = 0
for button_text in button_list:
    Button(window, text=button_text, width=5).grid(row=row_index, column = col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0

def click(key):
    if key == "=":
        resul = eval(display.get())
        s = str(result)
        display.insert(END, "="*s)
    else:
        display.insert(END, key)
        
row_index = 1
col_index = 0
for button_text in button_list:
    def process(t = button_text):
        click(t)
    Button(window, text = button_text, width=5, command=process).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
