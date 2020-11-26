# 리스트와 함수 예제 패턴퀴즈

def patternmatch(pattern, correctAns, wrongAns):
    for i in range(len(pattern)-1):
        print(pattern[i], end=" ")

    guessAns = int(input("다음 수는 무엇일까요? "))

    if guessAns == pattern[len(pattern)-1]:
        correctAns += 1
        print("잘 했어요. 축하해요")
    else:
        wrongAns += 1
        print("정답은 %d 입니다" %(pattern[len(pattern)-1]))
    return correctAns, wrongAns

correctAns = 0
wrongAns = 0

pattern1 = [2, 4, 6, 8]
pattern2 = [13, 16, 19, 22]
pattern3 = [2, 3, 5, 7, 11]
pattern4 = [1, 1, 2, 3, 5, 8]
pattern5 = [31, 28, 31, 30]

correctAns, wrongAns = patternmatch(pattern1, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern2, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern3, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern4, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern5, correctAns, wrongAns)

print("%d개 패턴중 %d개 맞았어요" %(correctAns + wrongAns, correctAns))


# 리스트와 함수 예제 패턴퀴즈2
import random

def patternmatch(pattern, correctAns, wrongAns):
    k = random.randint(0, len(pattern)-1)
    
    for i in range(len(pattern)):
        if i == k:
            print("?", end=" ")
        else:
            print(pattern[i], end=" ")
            
    guessAns = int(input("?에 들어갈 숫자는 무엇일까요? "))

    if guessAns == pattern[k]:
        correctAns += 1
        print("잘 했어요. 축하해요")
    else:
        wrongAns += 1
        print("정답은 %d 입니다" %(pattern[k]))
    return correctAns, wrongAns

correctAns = 0
wrongAns = 0

pattern = [[2, 4, 6, 8] , [13, 16, 19, 22], [2, 3, 5, 7, 11], [1, 1, 2, 3, 5, 8], [31, 28, 31, 30]]

for i in range(5):
    correctAns, wrongAns = patternmatch(pattern[i], correctAns, wrongAns)

print("%d개 패턴중 %d개 맞았어요" %(correctAns + wrongAns, correctAns))

