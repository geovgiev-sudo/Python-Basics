student = input()
klas = 1
score = 0
max_tries = 0

while True:
    new_score = float(input())
    if new_score < 4.00:
        max_tries += 1
        if max_tries > 1:
            print(f'{student} has been excluded at {klas} grade')
            break
        continue

    score += new_score
    if klas == 12:
        average_score = score / 12
        print(f'{student} graduated. Average grade: {average_score:.2f}')
        break
    klas += 1