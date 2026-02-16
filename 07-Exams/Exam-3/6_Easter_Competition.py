import sys

kozunaks_count = int(input())
points_max = -sys.maxsize
winner = ''

for kozunak in range(1, kozunaks_count + 1):

    baker_name = input()
    command = input()
    points = 0

    while command != 'Stop':
        kozunak_grade = int(command)
        points += kozunak_grade

        command = input()

    print(f'{baker_name} has {points} points.')

    if points > points_max:
        points_max = points
        winner = baker_name
        print(f'{baker_name} is the new number 1!')

print(f'{winner} won competition with {points_max} points!')