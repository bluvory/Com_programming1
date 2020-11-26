# 클래스 예제 성적처리

class Student:
    def __init__(self, name, midScore, finalScore, projectScore):
        self.name = name
        self.midScore = midScore
        self.finalScore = finalScore
        self.projectScore = projectScore

    def get_name(self):
        return self.name

    def get_sum(self):
        return self.sum

    def get_avg(self):
        return self.avg

    def calculate(self):
        self.sum = self.midScore + self.finalScore + self.projectScore
        self.avg = self.sum/3

    def get_grade(self):
        if self.avg >= 90:
            return "A"
        elif 80 <= self.avg < 90:
            return "B"
        elif 70 <= self.avg < 80:
            return "C"
        elif 60 <= self.avg < 70:
            return "D"
        else:
            return "F"

name = input("이름입력 : ")
midScore = int(input("중간 고사 성적 입력 : "))
finalScore = int(input("기말 고사 성적 입력 : "))
projectScore = int(input("과제 성적 입력 : "))

student1 = Student(name, midScore, finalScore, projectScore)

student1.calculate()
print("\n학생 이름=", student1.get_name())
print("합계=", student1.get_sum())
print("평균=", student1.get_avg())
print("등급=", student1.get_grade())

