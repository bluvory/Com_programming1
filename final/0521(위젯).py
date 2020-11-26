# 위젯
# 레이블 위젯
from tkinter import*
window = Tk()
label1 = Label(window, text = "GUI")
label2 = Label(window, text = "파이썬", font = ("굴림체", 20), fg = "blue")
label3 = Label(window, text = "공부중입니다", bg = "yellow", width = 20, height=5, anchor=SE)
# anchor : 위치 / SE : south east
label1.pack()
label2.pack()
label3.pack()
# pack이 있어야 화면상 보임
window.mainloop()


# 레이블에 글자 대신 이미지 넣기
from tkinter import*
window = Tk()
photo = PhotoImage(file = "images/rock.gif")
label1 = Label(window, image=photo)
label1.pack()
window.mainloop()


#
from tkinter import*
window = Tk()
photo = PhotoImage(file = "images/rock.gif")
label1 = Label(window, image=photo)
message = "가위바위보"
label2 = Label(window, justify = LEFT, padx = 10, text=message)
# justify : 정렬, padx : 띄어쓰기
label1.pack(side="right")
label2.pack(side="left")
window.mainloop()


# 버튼
from tkinter import*
window = Tk()
button1 = Button(window, text = "파이썬 종료", fg="red", command=quit)
button1.pack()
window.mainloop()


# 버튼의 텍스트 변경
from tkinter import*
window = Tk()
b1 = Button(window, text = "첫번째 버튼")
b1.pack()
b1["text"] = "one"
# b1의 text를 one으로 바꿔라
window.mainloop()


# 이미지 버튼을 누르면 간단한 메시지창이 나오는 코드
from tkinter import*
from tkinter import messagebox
def myFunc():
    messagebox.showinfo("가위바위보", "바위")
# messagebox.showinfo : 메시지창
window = Tk()
photo = PhotoImage(file="images/rock.gif")
button1 = Button(window, image=photo, command = myFunc)
button1.pack()
window.mainloop()


# 엔트리 위젯
from tkinter import*
window = Tk()
Label(window, text = "이름").pack(side="left")
Label(window, text = "나이").pack(side="left")
e1 = Entry(window)
e1.pack(side="right")
e2 = Entry(window)
e2.pack(side="right")
window.mainloop()


# 텍스트 위젯
from tkinter import*
window = Tk()
T = Text(window, height=5, width=60)
T.pack()
T.insert(END, "테스트 위젯은 여러줄의\n텍스트를 표시할 수 있습니다.")
mainloop()


# 체크버튼 : 켜고 끄는 데 사용하는 위젯
from tkinter import*
from tkinter import messagebox
window = Tk()

def myFunc():
    if chk.get() == 1:
        messagebox.showinfo("", "체크되었습니다")
    else:
        messagebox.showinfo("", "체크되지 않았습니다")

chk = IntVar()   # 정수형 변수를 형성한다
checkBtn = Checkbutton(window, text = "클릭하세요", variable=chk, command=myFunc)
# 체크 클릭하면 chk=1, 안하면 chk=0
checkBtn.pack()
window.mainloop()


# 라디오 버튼 : 여러개 중에서 하나를 선택하는 데 사용하는 위젯
from tkinter import*
window = Tk()
window.geometry("200x100")

def myFunc():
    if var.get() == 1:
        label1.configure(text = "파이썬")
    else:
        label1.configure(text = "C")
        
var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text = "C", variable=var, value=2, command=myFunc)
label1 = Label(window, text = "좋아하는 언어 : ", fg = "red")
rb1.pack()
rb2.pack()
label1.pack()
window.mainloop()


