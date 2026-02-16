eggs_painted = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for i in range(1, eggs_painted + 1):
    colour = input()

    if colour == 'red':
        red_eggs += 1

    elif colour == 'orange':
        orange_eggs += 1

    elif colour == 'blue':
        blue_eggs += 1

    elif colour == 'green':
        green_eggs += 1

max_count = red_eggs
max_colour = "red"

if orange_eggs > max_count:
    max_count = orange_eggs
    max_colour = "orange"

if blue_eggs > max_count:
    max_count = blue_eggs
    max_colour = "blue"

if green_eggs > max_count:
    max_count = green_eggs
    max_colour = "green"

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_count} -> {max_colour}')