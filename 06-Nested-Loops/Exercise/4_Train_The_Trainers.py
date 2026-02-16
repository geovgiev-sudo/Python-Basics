grades_count = int(input())
command = input()

presentation_count = 0
average_grade = 0
grades_total = 0
times_graded = 0

while command != 'Finish':
    presentation_name = command
    presentation_count += 1
    grade_per_presentation = 0

    for i in range(1, grades_count + 1):
        grade = float(input())
        grade_per_presentation += grade
        grades_total += grade
        times_graded += 1

    average_grade = grade_per_presentation / grades_count
    print(f'{presentation_name} - {average_grade:.2f}.')

    command = input()

average_score = grades_total / times_graded
print(f'Student\'s final assessment is {average_score:.2f}.')