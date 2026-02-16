minutes_walk = int(input())
number_of_walks = int(input())
calories_per_day = int(input())

minutes_total = minutes_walk * number_of_walks
total_calories_burned = minutes_total * 5
calories_enough = calories_per_day * 0.50

if total_calories_burned >= calories_enough:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.')

else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.')