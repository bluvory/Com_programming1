#초를 분으로 변경하시오.

seconds = int(input("초를 입력하시오"))

m = seconds // 60   #분구하기
s = seconds % 60

print("몇 ", m, "몇 ", s, 입니다)
