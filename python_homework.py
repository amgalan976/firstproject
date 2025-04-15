# ############################################
# 프로그램명: 성적관리 프로그램
# 작성자: 컴퓨터공학과 / 2024042032
# 작성일: 2025.04.15
# 프로그램 설명: 5명의 학생에 대해 영어, C언어, 파이썬 점수를 입력받아
# 총점, 평균, 학점, 등수를 계산하고 다양한 기능을 제공하는 프로그램
# ############################################

class Student:
    def __init__(self, student_id, name, eng, c_lang, python):
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.c_lang = c_lang
        self.python = python
        self.total = eng + c_lang + python
        self.avg = self.total / 3
        self.grade = self.get_grade()
        self.rank = 0

    def get_grade(self):
        if self.avg >= 90: return 'A'
        elif self.avg >= 80: return 'B'
        elif self.avg >= 70: return 'C'
        elif self.avg >= 60: return 'D'
        else: return 'F'

    def display(self):
        print(f"{self.student_id:<10}{self.name:<10}{self.eng:<8}{self.c_lang:<8}{self.python:<8}"
              f"{self.total:<8}{self.avg:<8.2f}{self.grade:<6}{self.rank:<6}")

class GradeManager:
    def __init__(self):
        self.students = []

    def input_students(self):
        for _ in range(5):
            student_id = input("학번 입력: ")
            name = input("이름 입력: ")
            eng = int(input("영어 점수: "))
            c_lang = int(input("C언어 점수: "))
            python = int(input("파이썬 점수: "))
            self.students.append(Student(student_id, name, eng, c_lang, python))
        self.calculate_ranks()

    def calculate_ranks(self):
        for s in self.students:
            s.rank = 1 + sum(1 for other in self.students if other.total > s.total)

    def display_students(self):
        print("\n학번       이름      영어    C언어   파이썬   총점    평균     학점   등수")
        print("----------------------------------------------------------------------")
        for s in self.students:
            s.display()

    def insert_student(self):
        student_id = input("학번 입력: ")
        name = input("이름 입력: ")
        eng = int(input("영어 점수: "))
        c_lang = int(input("C언어 점수: "))
        python = int(input("파이썬 점수: "))
        self.students.append(Student(student_id, name, eng, c_lang, python))
        self.calculate_ranks()

    def delete_student(self):
        student_id = input("삭제할 학번 입력: ")
        self.students = [s for s in self.students if s.student_id != student_id]
        self.calculate_ranks()

    def search_student(self):
        key = input("탐색할 학번 또는 이름 입력: ")
        found = [s for s in self.students if s.student_id == key or s.name == key]
        if found:
            print("\n탐색 결과:")
            print("학번       이름      영어    C언어   파이썬   총점    평균     학점   등수")
            print("----------------------------------------------------------------------")
            for s in found:
                s.display()
        else:
            print("학생을 찾을 수 없습니다.")

    def sort_by_total(self):
        self.students.sort(key=lambda s: s.total, reverse=True)
        self.calculate_ranks()

    def count_above_80(self):
        count = sum(1 for s in self.students if s.avg >= 80)
        print(f"\n평균 80점 이상 학생 수: {count}")

def main():
    manager = GradeManager()

    while True:
        print("\n[ 성적관리 프로그램 ]")
        print("1. 학생 정보 입력")
        print("2. 전체 출력")
        print("3. 학생 정보 삽입")
        print("4. 학생 정보 삭제")
        print("5. 학생 정보 탐색")
        print("6. 총점 기준 정렬")
        print("7. 80점 이상 학생 수 출력")
        print("0. 종료")
        choice = input("메뉴 선택: ")

        if choice == '1':
            manager.input_students()
        elif choice == '2':
            manager.display_students()
        elif choice == '3':
            manager.insert_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            manager.search_student()
        elif choice == '6':
            manager.sort_by_total()
        elif choice == '7':
            manager.count_above_80()
        elif choice == '0':
            print("프로그램 종료")
            break
        else:
            print("올바른 번호를 선택하세요.")

if __name__ == "__main__":
    main()
