# 객체지향
# 객체는 상태(속성)와 동작(기능)을 가진다 = 변수+메소드 ex.터틀쉑
# 객체의 설계도 작성 후 클래스로부터 객체 생성
# 클래스
# 빈클래스 만들기 class name: pass

# 객체의 사용 (변수, 메소드 사용하기) -> 객체.변수 / 객체.메소드()
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    def drive(self):
        self.speed = 60

myCar = Car(0, "blue", "E-class")
yourCar = Car(0, "white", "S-class")
myCar.drive()
yourCar.drive()

# 객제 생성하기1
class Car:
    def drive(self):
        self.speed = 10

myCar = Car()   # 객체 = 생성자
yourcar = Car()
myCar.color = "blue"
myCar.model = "E-Class"

myCar.drive()
print(myCar.speed)

# 객체 생성하기2
class Car:
    def drive(self):
        self.speed = 60

myCar = Car()
myCar.speed = 0
myCar.model = "E-class"
myCar.color = "blue"
myCar.year = "2020"

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)
print("자동차를 주행합니다.")
myCar.drive()
print("자동차의 속도는", myCar.speed)

# 객체 생성하기3
class Counter:
    def reset(self):
        self.count = 0
    def increment(self):
        self.count +=1
    def get(self):
        return self.count

a = Counter()
a.reset()
a.increment()
print("카운터 a의 값은", a.get())

# 하나의 클래스로 객체를 많이 만들 수 있다
a = Counter()
b = Counter()
a.reset()
b.reset()
a.increment()
for i in range(5):
    b.increment()
a.get()
b.get()

# 객체를 생성하면서 초기화하기 : 생성자 ( __init__ ) 초기값주고싶으면만들기
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed   # 객체.속성 = 외부에서 주어지는 변수
        self.color = color
        self.model = model

class Person:
    def __init__(self, name, age, address):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print("{0} 나는 {1} 입니다".format(self.hello, self.name))

jjanggu = Person("신짱구", 5, "떡잎마을")
jjanggu.greeting()
print("이름", jjanggu.name)
print("나이", jjanggu.age)
print("주소", jjanggu.address)

# 소멸자
class Car:
    def __del__(self):
        print(self.model + "객체가 소멸됩니다")

myCar = Car()
del myCar
# print(myCar.speed) = 없다고 나옴 왜냐면 소멸되었기때문에


# 메소드 정의 (클래스안에 정의된 함수, 첫번째 매개변수는 항상 self여야 한다)
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed   
        self.color = color
        self.model = model
    def drive(self):
        self.speed = 60
    def getShow(self):
        return self.color, self.model
    
dadCar = Car(0, "silver", "A6")
momCar = Car(0, "white", "520d")
myCar = Car(0, "blue", "E-class")
dadCar.drive()
myCar.getShow()


# 메소드 호출
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel):
        self.channel = channel
    def getChannel(self):
        return self.channel

t = Television(9, 10, True)
t.show()
t.setChannel(11)
t.show()

# __str__() 메소드 : 문자열로 반환하는 역할
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed   
        self.color = color
        self.model = model
    def __str__(self):
        msg = "속도:" + str(self.speed) + " 색상:" + self.color + " 모델:" + self.model
        return msg
    
myCar = Car(0, "blue", "E-class")
print(myCar)

