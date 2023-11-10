# https://www.acmicpc.net/problem/25206

total = []
total_credit = 0
total_grade = 0
GRADE = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0,
}

for subject in range(20):
    total.append(input().split())

for grade in total:
    if grade[2] == 'P':
        pass
    else:
        total_grade += int(grade[1][0]) * GRADE[grade[2]]
        total_credit += int(grade[1][0])

print(round(total_grade / total_credit, 6))