name = input()
klas = 1
grade_total = 0
average_grade = 0
max_tries = 0
while True:
    yearly_grade = float(input())
    grade_total += yearly_grade
    if klas == 12:
        average_grade = grade_total / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break

    if yearly_grade < 4:
        max_tries += 1
        if max_tries > 1:
            print(f'{name} has been excluded at {klas} grade')
            break
        continue

    klas += 1




# print(f'{name} graduated. Average grade: {average_grade:.2f}')
# print(f'{name} has been excluded at {grade} grade')