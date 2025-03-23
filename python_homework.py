def input_student_data():
    students = []
    for _ in range(5):
        student = {}
        student['학번'] = input("학번: ")
        student['이름'] = input("이름: ")
        student['영어'] = int(input("영어: "))
        student['C-언어'] = int(input("C-언어: "))
        student['파이썬'] = int(input("파이썬: "))
        students.append(student)
    return students

def calculate_scores(students):
    for student in students:
        student['총점'] = student['영어'] + student['C-언어'] + student['파이썬']
        student['평균'] = student['총점'] // 3
        student['학점'] = calculate_grade(student['평균'])
    students.sort(key=lambda x: x['평균'], reverse=True)
    for rank, student in enumerate(students, start=1):
        student['등수'] = rank

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B+'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'F'

def display_results(students):
    print("\n성적관리 프로그램")
    print("=" * 75)
    print("학번        이름    영어  C-언어  파이썬  총점  평균  학점  등수")
    print("=" * 75)
    for student in students:
        print(f"{student['학번']}  {student['이름']:4}  {student['영어']:3}   {student['C-언어']:3}    {student['파이썬']:3}   {student['총점']:3}   {student['평균']:3}  {student['학점']:3}  {student['등수']:3}")

students = input_student_data()
calculate_scores(students)
display_results(students)
