students = int(input())
s1 = 0
s2 = 0
s3 = 0
s4 = 0
grades_total = 0

for i in range(students):
    grade = float(input())
    grades_total += grade
    if 2 <= grade <= 2.99:
        s1 += 1
    elif 3 <= grade <= 3.99:
        s2 += 1
    elif 4 <= grade <= 4.99:
        s3 += 1
    elif 5 <= grade:
        s4 += 1

s4_percent = f'{s4 / students * 100:.2f}%'
print(f'Top students: {s4_percent}')

s3_percent = f'{s3 / students * 100:.2f}%'
print(f'Between 4.00 and 4.99: {s3_percent}')

s2_percent = f'{s2 / students * 100:.2f}%'
print(f'Between 3.00 and 3.99: {s2_percent}')

s1_percent = f'{s1 / students * 100:.2f}%'
print(f'Fail: {s1_percent}')

grades_average = grades_total / students
print(f'Average: {grades_average:.2f}')