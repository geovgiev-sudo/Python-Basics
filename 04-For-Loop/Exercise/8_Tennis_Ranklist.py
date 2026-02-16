from math import floor

tournaments = int(input())
starting_points = int(input())

total_points = starting_points
points_from_tournaments = 0
wins = 0

for _ in range(1, tournaments + 1):
    result = input()
    if result == 'W':
        total_points += 2000
        points_from_tournaments += 2000
        wins += 1
    if result == 'F':
        total_points += 1200
        points_from_tournaments += 1200
    if result == 'SF':
        total_points += 720
        points_from_tournaments += 720

average_points = points_from_tournaments / tournaments
win_percentage = wins / tournaments * 100

print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points)}')
print(f'{win_percentage:.2f}%')
