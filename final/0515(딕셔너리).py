# 딕셔너리 (value와 key로 구성)
phonebook = {}  # 공백 딕셔너리
phonebook["홍길동"] = "01012345678"
print(phonebook)

phonebook = {"홍길동":"01012345678"}
phonebook["강감찬"] = "0101235679"
phonebook["이순신"] = "01012345680"
print(phonebook)

# 딕셔너리 키로 탐색
print(phonebook["강감찬"])

# get()으로 탐색 (key에 대응되는 value 반환)
print( phonebook.get("홍길동") )

# 모든 키 출력하기 key()
print( phonebook.keys() )
print( list(phonebook.keys()) )

# 모든 값 출력하기 values()
print( phonebook.values() )

# 한 학생에 대한 정보를 딕셔너리로 저장
dict = {"name":"홍길동", "age":7, "class":"초급"}
print( dict["name"] )
print( dict["age"] )

# 딕셔너리 항목 방문 후 출력
for k in phonebook.keys():
    print(k)
for v in phonebook.values():
    print(v)

# 딕셔너리 항목 방문 후 출력2
for k in phonebook.keys():
    print(k, phonebook[k])
for k in sorted( phonebook.keys() ):   # 정렬 후 출력
    print(k, phonebook[k])


# key와 value를 한꺼번에 보여줄때 items()
info = {"name" : "장재경", "phone" : "010-0000-0000"}
print( info.items() )

# 항목 삭제 del
del phonebook["홍길동"]
print(phonebook)

# 모든 항목 삭제 clear()
phonebook.clear()
print(phonebook)

# 존재 여부 판단 in연산자
print( "신짱구" in phonebook )

# 평균 점수 구하기
midterm = {"java":30, "python":50, "os":40}
print("과목명 점수")
for key, value in midterm.items():
    print("%-6s %5d" %(key, value))   #왼쪽맞춤 -6
print("-"*20)
avg = sum(midterm.values()) / len(midterm)
print("평균 = ", avg)

