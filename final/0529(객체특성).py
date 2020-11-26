# 상속 : 클래스를 정의할때 부모 클래스를 지정하는 것

from turtle import*
class MyTurtle(Turtle):
    def glow(self, x, y):
        self.fillcolor("red")
turtle = MyTurtle()
turtle.shape("turtle")
turtle.onclick(turtle.glow)   # 거북이 클릭하면 색상이 빨강색으로 변경

#
class Person:
    def greeting(self):
        print("안녕하세요")

class Student(Person):
    def study(self):
        print("공부하기")

jk = Person()
jg = Student()
jg.greeting()
jg.study()
jk.greeting()
jk.study()  # 오류

# 정보은닉 (구현의 세부 사항을 클래스 안에 감추는 것) : __어쩌구
class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
        def getWallet(self):
            return jg.__wallet
        
jg = Person("신짱구", 5, "떡잎마을", 10000)
print(jg.name)
#print(jg.__wallet)
print(jg.getWallet())


# 접근자 : 인스턴스 변수값을 반환 (get으로 시작)
# 설정자 : 인스턴스 변수값을 설정 (set으로 시작)
class Student:
    def __init__(self, name = None, age=0):
        self.__name = name
        self.__age = age
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self, age):
        self.__age = age
    def setName(self, name):
        self.__name = name
        
obj = Student("Hong", 20)
print(obj.getName())

# 터틀그래픽보기
# 상위 클래스 : super()
