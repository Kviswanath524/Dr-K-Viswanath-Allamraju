# Exam Grading System (Alternative Method)

score = int(input())

grade_scale = {
    "A": range(90, 101),
    "B": range(80, 90),
    "C": range(70, 80),
    "D": range(60, 70),
    "F": range(0, 60)
}

for grade, marks in grade_scale.items():
    if score in marks:
        print(grade)
        break
