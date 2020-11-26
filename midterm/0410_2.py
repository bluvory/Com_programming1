'''
sum = 0
for i in range(1, 101):
    sum = sum + i     # sum += i
print("1부터", i, "까지 합 = ", sum)


# 짝수합
sum = 0
for i in range(0, 101, 2):
    sum = sum + i     # sum += i
print("1부터", i, "까지 합 = ", sum)


# 짝수합, 홀수합
sum = 0
evenSum = 0
oddSum = 0
for i in range(0, 101):
    sum = sum + i

    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
        
print("1부터", i, "까지 합 = ", sum)
print("1부터", i, "까지 홀수합 = ", oddSum)
print("1부터", i, "까지 짝수합 = ", evenSum)


print("-"*50)


# while 써서 구하기
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print("while문 : 1부터", i-1, "까지 합 = ", sum)



sum = 0
num = int(input("어떤 수를 입력하시오"))
while num >= 0:
    sum += num
    num = int(input("어떤 수를 입력하시오"))
print("데이터합 = ", sum)


print("="*100)


sum = 0
while True:
    num = int(input("어떤 수를 입력하시오"))
    if num >= 0:
        sum += num
    else:
        break
print("데이터합 = ", sum)

        

colors = ["red", "green", "blue"]
for color in colors:
    print(color, end = " ")



for x in range(5):
    for i in range(10):
        print("*", end=" ")
    print()


i = 1
while i <= 10:
    print("?", end = " ")
    i += 1
'''

x = 1
while x <= 5:
    i = 1
    while i <= 10:
        print("?", end = " ")
        i += 1
    print()
    x += 1








