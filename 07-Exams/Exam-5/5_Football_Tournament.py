team_name = input()
games_played = int(input())
points = 0
points_total = 0
win_counter = 0
draw_counter = 0
lose_counter = 0

if games_played == 0:
    print(f'{team_name} hasn\'t played any games during this season.')
    exit()

for i in range(1, games_played + 1):
    result = input()

    if result == 'W':
        points = 3
        points_total += points
        win_counter += 1

    elif result == 'D':
        points = 1
        points_total += points
        draw_counter += 1

    elif result == 'L':
        lose_counter += 1

win_percentage = win_counter / games_played * 100
print(f'{team_name} has won {points_total} points during this season.')
print(f'Total stats:')
print(f'## W: {win_counter}')
print(f'## D: {draw_counter}')
print(f'## L: {lose_counter}')
print(f'Win rate: {win_percentage:.2f}%')
