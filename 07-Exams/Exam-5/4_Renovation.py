from math import ceil

wall_height = int(input())
wall_width = int(input())
protzent_unpainted = int(input())
command = input()

area = wall_height * wall_width * 4
area_to_paint = ceil(area - (area * protzent_unpainted / 100))

while command != 'Tired!':
    litres_of_paint = int(command)
    area_to_paint = area_to_paint - litres_of_paint

    if area_to_paint == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break

    if area_to_paint < 0:
        paint_left = abs(area_to_paint)
        print(f'All walls are painted and you have {paint_left} l paint left!')
        break

    command = input()

else:
    print(f'{area_to_paint} quadratic m left.')
