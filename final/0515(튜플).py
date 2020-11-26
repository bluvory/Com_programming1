# 튜플 ( 값 변경 안됨, 값 하나면 무조건 마지막에 콤마 )
a, b = ("new", "python")
(a, b) = ("new", "python")
(a, b) = "new", "python"

a, b = (10, 20)
print(a)
a, b = b, a
print(a)

# 항목 탐색
t1 = (1, 2, "a", "b")
print( t1[0] )
print( t1[3] )

# 슬라이싱
t1 = (1, 2, "a", "b")
print( t1[1:] )


# 더하기
t1 = (1, 2, "a", "b")
t2 = (3, 4)
print( t1 + t2 )

# 곱하기
t2 = (3, 4)
print( t2 * 3 )

# 길이 구하기
t1 = (1, 2, "a", "b")
print( len(t1) )


# 튜플 활용: 여러개의 값을 반환할때 사용
def calc(a, b):
    c = a + b
    d = a - b
    return (c, d)
total, sub = calc(10, 20)
print("sum = ", total)
print("sub = ", sub)

# 집합 자료형 (중복 허용X, 순서 없음 -> index로 접근 불가 따라서 list로 바꾸면 됨)
s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2)

# 교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print( s1 & s2 )
print( s1.intersection(s2) )

# 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print( s1 | s2 )
print( s1.union(s2) )

# 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print( s1 - s2 )
print( s2 - s1 )
print( s1.difference(s2) )
print( s2.difference(s1) )

# 값 1개 추가 add
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가 update
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기 remove (index 없으니까 값으로 제거)
s1 = set([1,2,3])
s1.remove(2)
print(s1)

