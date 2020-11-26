# 모듈과 파일입출력 여행지 퀴즈 게임기

from tkinter import*
window = Tk()
window.title("퀴즈 풀기")
window.geometry("400x350+10+10")
qlabel = Label(window, width=10, text="")
qlabel.pack()
ilabel = Label(window)
ilabel.pack()
Label(window, text="정답을 쓰고 [Enter]키를 누르시오.").pack()
rlabel = Label(window)
rlabel.pack()

file = open("problem.txt", "r", encoding='utf-8')
p = file.readlines()
file.close()

i = -1
answer=""

def checkanswer(event):
    global answer, e
    if answer==e.get():
        rlabel.config(text="정답입니다")
    else:
        rlabel.config(text="오답입니다")

e = Entry(window, width=50)
e.bind("<Return>", checkanswer)
e.pack()

def getQuestion():
    global i, answer, e
    i += 1
    if i>=4:
        i=0
    e.delete(0, len(e.get()))
    rlabel.config(text="")

    aQuestion = p[i].strip()
    Q = aQuestion.split(":")

    qlabel.config(text=Q[0])
    answer = Q[1]
    img = PhotoImage(file=Q[2])
    ilabel.config(image=img)
    ilabel.image = img
    

Button(window, text="다음 문제", command=getQuestion).pack()
getQuestion()
window.mainloop()

