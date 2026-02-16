from math import ceil, floor

days = int(input())
food = int(input())
dog_per_day = float(input())
cat_per_day = float(input())
turtle_per_day_grams = float(input())

dog_eats = days * dog_per_day
cat_eats = days * cat_per_day
turtle_eats = days * (turtle_per_day_grams / 1000)
total_eaten = dog_eats + cat_eats + turtle_eats

if total_eaten <= food:
    food_left = food - total_eaten
    print(f'{floor(food_left)} kilos of food left.')
else:
    food_needed = total_eaten - food
    print(f'{ceil(food_needed)} more kilos of food are needed.')
