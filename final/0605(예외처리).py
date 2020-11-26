# 예외처리

# 오류
# 구문 오류 Syntax Error
# 예외 오류 Exception / 런타임 오류 Runtime Error

x,y=2,0
try:
    z=x/y
except ZeroDivisionError:
    print("0으로 나누는 예외")

x,y=2,0
try:
    z=x/y
except ZeroDivisionError as e:
    print(e)


while True:
    try:
        n = input("숫자를 입력하시오: ")
        n = int(n)
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오")
print("정수 입력이 성공하였습니다!")


try:
    fname = input("파일 이름을 입력하세요: ")
    infile = open(fname, "r")
except IOError:
    print("파일 " + fname + "을 발견할 수 없습니다")


# 다중 예외 처리 구조
try:
    fn = open("testfile", "w")
    fh.write("테스트 데이터를 파일에 씁니다!!")
except IOError:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
else:
    print("파일에 성공적으로 기록하였습니다")
    fh.close()

# 예외가 기술되지 않은 except 블록
try:
    fn = open("testfile", "w")
    fh.write("테스트 데이터를 파일에 씁니다!!")
except:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
else:
    print("파일에 성공적으로 기록하였습니다")
    fh.close()
    

# 여러개의 예외를 가지는 except 블록
try:
    fn = open("testfile", "w")
    fh.write("테스트 데이터를 파일에 씁니다!!")
except (Exception1[, Exception2[, ... ExceptionN]]:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
else:
    print("파일에 성공적으로 기록하였습니다")
    fh.close()


# try-finally 블록
x = int(input("정수를 입력하시오"))
y = int(input("정수를 입력하시오"))

try:
    result = x/y
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except ValueError:
    print("정수가 아닙니다. 다시 입력하시오")
else:
    print("result = %0.2f" %result)
finally:
    print("넌 누구니?")


# 예외 발생하기
try:
    n = int(input("양의 정수를 입력하세요"))
    m = int(input("양의 정수를 입력하세요"))
    if n<=0 or m<0:
        raise ArithmeticError("두 수 중 하나가 0이하이다")
except ArithmeticError as e:
    print("예외 처리 발생: ", e)





    
