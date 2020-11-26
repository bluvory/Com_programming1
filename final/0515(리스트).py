# 리스트는 객체 (객체는 관련되는 변수와 함수를 묶은 것 ex 점)

# 리스트 기초
list1 = [6,8,2,9,1,8,2]
print( min(list1) )  # 최소
print( max(list1) )  # 최대

# 리스트 요소 추가 append
heroes = []
heroes.append("아이언맨")
print(heroes)

# 리스트 얕은 복사
a = [2, 4, 5]
b = a
print(b)
b[1] = 9
print(a)
print(b)

# 리스트 깊은 복사
a = [2, 4, 5]
b = list(a)
print(a)
print(b)
b[1] = 9
print(a)
print(b)

# 리스트 함축 (express for 변수 in old_list 조건)
list1 = [ x**2 for x in range(10) ]
print(list1)

list1 = [ x**2 for x in range(10) if x%2==0 ]
print(list1)

list1 = ["Python", "C", "Java", "C++"]
first_char = [ch[0] for ch in list1]
print(first_char)

# 슬라이싱(한번에 여러개의 항목을 추출하는 기법)
letters = ['A', 'B', 'C', 'D', 'E', 'F']
print( letters[0:3] )
print( letters[:3] )
print( letters[3:] )
print( letters[:] )

# append()는 맨뒤에 추가
# insert()는 원하는 위치에 추가 ex_insert(1, "배트맨")

# 리스트 항목 삭제하기 remove()
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
if "스칼렛 위치" in heroes:
    heroes.remove("스칼렛 위치")
print(heroes)

# 리스트 항목 삭제하기  del
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
del heroes[0]
print(heroes)

a = [1,2,3,4,5]
del a[2:]
print(a)

# 리스트 항목 삭제하기 pop()
# pop() : 리스트에서 마지막 항목을 삭제
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
last_hero = heroes.pop()
print(last_hero)

# pop(x) : 리스트의 x번째 항목 삭제
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
name = heroes.pop(1)
print(name)
print(heroes)


# 리스트 항목 변경하기
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes[1] = "닥터 스트레인지"
print(heroes)


# 리스트 탐색하기 index()
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
if "헐크" in heroes:
    print(heroes.index("헐크"))
    
for hero in heroes:
    print(hero)


# 리스트 정렬하기 sort(), sorted
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes.sort()
print(heroes)  # 리스트 자체가 바껴버림 -> 깊은 복사 사용

numbers = [1, 8, 2, 5, 11, 23, 9]
numbers.sort()
print(numbers)

numbers = [1, 8, 2, 5, 11, 23, 9]
new_num = sorted(numbers)
print(new_num)


# 이중 리스트
numbers = [1, 3, 5, ['a', 'b', 'c']]
print(numbers)
print(numbers[0])
print(numbers[3][1])
for x in numbers:
    print(x)
for x in numbers[3]:
    print(x)


# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)


# 리스트 길이구하기 len()
a = [1, 2, 3]
print( len(a) )

# 리스트 요소 개수 세기 count()
msg = ['a', 'b', 'c', 'a', 'a', 'b']
print( msg.count('a') )

# 리스트 역순 reverse()
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 리스트 위치반환 index()
msg = ['a', 'b', 'c']
print( msg.index('b') )
print( msg.index('c') )

# 리스트 확장하기 extend()
msg = ['a', 'b', 'c']
msg.extend([1, 2])
print(msg)


# 이중 리스트 (2차원적으로 나타낼때 ex 표)
a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
row = len(a)    # 행의 개수
col = len(a[0])  # 열의 개수

for r in range(row):
    for c in range(col):
        print("%5d" %a[r][c], end = ",")
    print()


#Lab : 오륜기 그리기
import turtle

def dos():
    positions = [[0,0,"blue"], [-120,0,"purple"], [60,60,"red"], [-60,60,"yellow"], [-180,60,"green"]]
    for x,y,c in positions:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.color(c,c)
        t.begin_fill()
        t.circle(30)
        t.end_fill()

t = turtle.Turtle()
dos()

# 주사위 합 구하기
rows = 6
cols = 6
table = []
for row in range(rows):
    table += [[0] * cols]
for row in range(rows):
    for col in range(cols):
        table[row][col] = row+1+col+1
print(table)


    
