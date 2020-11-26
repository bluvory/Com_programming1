# tkinter로 GUI 만들기
# 위젯 사용해서 인터페이스를 만듦

# 버튼이 있는 윈도우 생성
# from <모듈> import <가져오고 싶은 변수 또는 함수>
from tkinter import*
window = Tk()   # 루트 윈도우 생성
button = Button(window, text = "클릭하세요!")
button.pack()
window.mainloop()

import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="클릭하세요!")
button.pack()
window.mainloop()

from tkinter import*
window = Tk()
label = Label(window, text = "Hellow World!")
label.pack()
window.mainloop()

from tkinter import*
window = Tk()
window.title("윈도 창 연습")
window.geometry("400x100")
window.resizable(width = FALSE, height = FALSE)  # 변경 불가
window.mainloop()

# 엔트리와 레이블 위젯 사용
from tkinter import*
window = Tk()
l1 = Label(window, text = "화씨")
l2 = Label(window, text = "섭씨")
l1.pack()
l2.pack()

e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()

b1 = Button(window, text="화씨->섭씨")
b2 = Button(window, text="섭씨->화씨")
b1.pack()
b2.pack()

window.mainloop()

# gui 실습
from tkinter import*
from tkinter import messagebox
window = Tk()
window.title("새창")
window.geometry("600x600")
button = Button(window, text = "click", fg="red", bg="green")
button.pack()
label = Label(window, text="파이썬조아", width=300, font=("나눔고딕", 40), fg="blue")
label.pack()

def process():
    if chk.get() == 1:
        messagebox.showinfo("확인되었음")
    else:
        messagebox.showinfo("확인불가")
chk = IntVar()
chkBtn = Checkbutton(window, text = "대중교통", variable=chk, command = process)
chkBtn.pack()
window.mainloop()




