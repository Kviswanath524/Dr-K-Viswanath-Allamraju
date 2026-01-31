# Exam Grading System (Using Integer Division)

score = int(input())

if score >= 60:
    print(["D", "C", "B", "A"][min(score // 10 - 6, 3)])
else:
    print("F")
