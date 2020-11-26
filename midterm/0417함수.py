def sum(a, b):
    res = a+b
    return res
a = sum(3, 4)
print(a)


def get_max(a,b,c):
    if a>b:
        max = a
    else:
        max = b
    if max < c:
        max=c
    return max
k = get_max(6,9,2)
print(k)


def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)


def even_odd(num):
    if num%2==0:
        print("짝수이다")
        return 1
    else:
        print("홀수이다")S
        return 0


def get_hi(name, msg="안녕"):
    print(name + msg)
get_hi("장재경")
get_hi("신짱구", "잘가")


def print_address():
    print("서울특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print("홍길동")

print_address()


def calculate_area(radius):
    area = 3.14*raius**2
    return area


def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum


import turtle
t = turtle.Turtle()

# n-각형 그리는 함수를 정의한다
def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)
for i in range(10):
    t.left(20)
    n_polygon(6,100)


def calculate_area(radius):
    global area
    area = 3.14*radius**2
    return

area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print(area)


def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다" % name)
    print("나이는 %d살입니다" % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")


