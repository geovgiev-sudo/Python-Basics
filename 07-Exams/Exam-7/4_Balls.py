from math import floor

balls_count = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colours = 0
divides_from_black = 0

for ball in range(1, balls_count + 1):
    colour = input()
    if colour == 'red':
        points += 5
        red_balls += 1
    elif colour == 'orange':
        points += 10
        orange_balls += 1
    elif colour == 'yellow':
        points += 15
        yellow_balls += 1
    elif colour == 'white':
        points += 20
        white_balls += 1
    elif colour == 'black':
        points = floor(points / 2)
        divides_from_black += 1
    else:
        other_colours += 1

print(f'Total points: {points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_colours}')
print(f'Divides from black balls: {divides_from_black}')