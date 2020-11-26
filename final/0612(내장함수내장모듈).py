
# 내장함수

# abs(x) 절댓값
abs(3)=3 , abs(-3)=3

# pow(x, y) x의 y제곱 = x**y
pow(2, 4)=16 , pow(3, 3)=27

# sum() 합
sum([1, 2, 3])=6

# hex(x) 16진수(0x : 16진수)
hex(234)='0xea' , hex(3)='0x3'

# all 모두가 참인가
all([1,2,3])=True , all([1,2,3,0])=False -> 0이 False이기때문에

# any 적어도 하나는 참인가
any([1,2,3,0])=True , any([0, ""])=False

# dir 객체가 가지고 있는 함수나 변수를 나열
dir([1,2,3]) = ['append', 'count', 'extend', 'index', 'insert', 'pop', ..]

# eval 문자로 구성되어진 수식의 합
eval('1+2') = 3
eval(" 'hi' + 'a' ") = 'hia'
eval('divmod(4, 3)') = (1, 1)

# len 수치는 들어갈 수 없음
len("python")=6 , len([1,2,3])=6 , len((1, 'a'))=2

# list 리스트로 변환
list('python') = ['p', 'y', 't', 'h', 'o', 'n'] , list((1,2,3)) = [1,2,3]

# tuple 튜플로 변환
tuple("abc") = ('a', 'b', 'c') , tuple([1,2,3])=(1,2,3)

# isinstance 자료형에 속하는가
class Person: pass
a = Person()
isinstance(a, Person) = True

# max(iterable) 최댓값
max([1,2,3])=3 , max("python")='y'

# min(iterable) 최솟값
max([1,2,3])=1 , max("python")='h'

# divmod(x, y) 몫과 나머지
divmod(7, 3)=(2, 1) , divmod(1.3, 0.2)=(3.0, 0.09999999978)

# round(number, [,ndigits]) (소숫점 아래 몇째 자릿수까지) 반올림
round(4.6)=5 , round(5.678, 2)=5.68

# ord() 코드 -> 아스키코드
ord('a')=97 , ord('0')=48

# chr() 아스키코드 -> 코드
chr(97)='a' , chr(48)='0'

# map(f, iterable)
def two_times(x):
    return x*2
list(map(two_times, [1,2,3,4])) = [2,4,6,8]

# filter(f, iterable)
def positive(x):
    return x>0
print(list(filter(positive, [1,-3,2,0,-5,6]))) = [1,2,6]

# lambda 함수def를 간결하게 만날때 사용
# lambda 매개변수1, 2, ... : 매개변수를 사용한 표현식
add = lambda a,b : a+b
add(3,4)=7


# 내장모듈
# 파일과 디렉터리 접근 : sys, os
# 데이터 파일 저장 : pickle
# 수학 및 랜덤 : math, random
# 인터넷 액세스 : webbrowser, urllib
# 날짜와 시간 : time, datetime


# math 모듈
# floor(x) : x의 내림 연산
# sin(x) : sinx값 반환
# pi : 원주율 반환
# trunc(x) : x의 정수부분만 반환
# factorial(x) : x의 팩토리얼 값 반환
# hypot(x, y) : (0, 0)에서 (x, y)까지의 거리 반환
# log(x) : 로그 연산
# degrees(x) : 라디안을 각도 값으로 변환
# e : 자연상수 값 반환
# copyign(x, y) : y의 부호를 복사하여 x로
# fsum(a) : 값들의 합계 반환
# gcd(x, y) : 두 수의 최대 공약수

# sys 모듈 : 명령 매개변수 받을 대 자주 사용
import sys
print(sys.argv)

# pickle 모듈 : 객체의 형태를 그대로 사용하면서 파일에 저장하고 불러올 수 있게 함

# os 모듈 : 운영체제 관련 기능 모듈 (새폴더 만들기, 폴더 내부 파일 목록 열람)
os.getcwd()  # 현재디렉터리 확인
os.chdir("test")  # 새 경로로 전환
os.listdir()  # 현재 디렉터리 파일 출력
os.mkdir("text folder")  # 파일 만들기
os.rename('text.py', 'os_text_of.py')  # 디렉터리 이름 바꾸기
os.remove('os_text_of.py')  # 디렉터리 삭제하기
os.rmdir('text folder')  # 디렉터리 경로 삭제

# datetime 모듈 : 오늘 날짜 확인
import datetime
datetime.date.today()
d = datetime.date.today()
d.year, d.month, d.day, d.max
d.isoformat()   #yyyy-mm-dd 형태로 반환
d.ctime()  # 날짜와 시간을 출력, 시간은 00:00:00로 초기화
d.strftime("%y년 %m월인데 %d일겁니다")  # 표시 형태대로 출력

# time 모듈
import time
time.time()
time.local(time.time())
time.sleep(1)  # 실행속도 제어

# webbrowser : 웹 브라우저에서 특정 사이트 열어보기
import webbrowser
webbrowser.open("http://www.google.com")

# rullib : 웹에 있는 데이터 이용하기
import urllib.request
target = urllib.request.urlopen("https://google.com")
output = target.read()
output2 = target.getheaders()   #서버에 관한 자료 불러오기
print(output)
target.status # 정상적으로 열렸는지 확인(200)
# urllib.reques : url을 읽고, 열고, 정보를 얻는다
# urllib.error : request에 의해 발생하는 예외를 포함
# urllib.parse : URL 구문 분석을 위한 도구를 제공한다
# urllib.robotparser : 관리자가 민감한 정보들을 미리 적어둔 robots.txt를 분석


