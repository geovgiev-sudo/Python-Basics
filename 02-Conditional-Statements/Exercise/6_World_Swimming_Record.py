import math
from math import floor

world_record = float(input())
metres_to_swim = float(input())
seconds_per_metre = float(input())

time = metres_to_swim * seconds_per_metre
slow_downs = floor(metres_to_swim / 15)

# Изчисляваме колко пъти ще бъде забавян (на всеки 15 метра)
# и закръгляме надолу до най-близкото цяло число

time_slower = slow_downs * 12.5

# На всеки 15 метра му се добавят по 12.5 секунди на метър

time_total = time + time_slower
difference = abs(time_total - world_record)

# абсолютна стойност - изчисляваме разликата между рекорда и времето на Иван

if time_total < world_record:
    print(f'Yes, he succeeded! The new world record is {time_total:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')