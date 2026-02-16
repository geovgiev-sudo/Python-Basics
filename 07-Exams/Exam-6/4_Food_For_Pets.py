days = int(input())
food = float(input())
food_eaten_total = 0
total_biscuits_eaten = 0
dog_total = 0
cat_total = 0

for day in range(1, days + 1):
    dog_eat = int(input())
    cat_eat = int(input())
    dog_total += dog_eat
    cat_total += cat_eat
    food_eaten_today = dog_eat + cat_eat
    food_eaten_total += food_eaten_today
    if day % 3 == 0:
        biscuits_eaten_today = food_eaten_today * 0.10
        total_biscuits_eaten += biscuits_eaten_today

protzent_eaten_total = food_eaten_total / food * 100
protzent_eaten_dog = dog_total / food_eaten_total * 100
protzent_eaten_cat = cat_total / food_eaten_total * 100
print(f'Total eaten biscuits: {round(total_biscuits_eaten)}gr.')
print(f'{protzent_eaten_total:.2f}% of the food has been eaten.')
print(f'{protzent_eaten_dog:.2f}% eaten from the dog.')
print(f'{protzent_eaten_cat:.2f}% eaten from the cat.')
