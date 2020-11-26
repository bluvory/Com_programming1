
# 라이브러리 : 파이썬이 제공하는 내장 함수
# 모듈 : 함수나 변수 또는 크래스를 모아놓은 파일

import mod1
total = mod1.sum(5, 6)
print("두 수의 합 = ", total)

# 모듈명이 길어서 불편할때

# from 모듈이름 import 가져오고싶은것
# 다 가지고 오고싶으면 import *
# 모듈명 생략 가능
from mod1 import sum
total = sum(5, 6)
print("두 수의 합 = ", total)

# import 모듈 as 사용하고싶은식별자
# 모듈명 이름 줄여서 사용
import mod1 as m
total = m.sum(5, 6)
print("두 수의 합 = ", total)


# LAB 원 관련 모듈
import circle_mod
r = circle_mod.number_input()
print("반지름이 %.2f 인 원의 둘레는 %.2f이다" %(r, circle_mod.get_circumference(r)))


# if __name__ == "__main__"
# 다른 파일에서 모듈 실행할때 내 함수에서 쓴건 출력 안되게 하는 것 (내파일에선 실행됨)
# print(__name__) = __name__ 인데 다른파일에서 실행할땐 false가 됨


# 패키지 : 파이썬 모듈이 모여 이룬 것
# __init__ 이 있어야 파일을 열 수 있음
# import 뒤에 함수이름 못씀 모듈이름이나 패키지이름으로 끝나야함
# 폴더단위로 자를땐 __init__파일에 __all__ = ['display'] 써야함



