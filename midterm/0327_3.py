a = 10
b = 5

a += 100
b **= 3

print(a)
print(b)

x = 6
y = 8

print("6 > 8 ?", x > y)
print("6 = 8 ?", x == y)
print("6 != 8 ?", x != y)

print("안녕" * 10)

if x % 2 == 0:
    print(x, "짝수이다")
else:
    print(x, "홀수이다")


number = int(input("세 자리 정수를 입력하시오"))
n1 = number // 100
n2 = number % 100 // 10
n3 = number % 10



