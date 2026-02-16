import sys
command = input()
max_score = -sys.maxsize
best_player = ''

while command != 'END':
    player_name = command
    goals_scored = int(input())

    if goals_scored > max_score:
        max_score = goals_scored
        best_player = player_name

    if goals_scored >= 10:
        break

    command = input()

print(f'{best_player} is the best player!')
if max_score >= 3:
    print(f'He has scored {max_score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_score} goals.')
