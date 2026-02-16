food_bought = int(input())
food_bought_grams = food_bought * 1000
command = input()
grams_eaten = 0
while command != 'Adopted':
    grams_per_eat = int(command)
    grams_eaten += grams_per_eat
    command = input()

if grams_eaten <= food_bought_grams:
    food_left = food_bought_grams - grams_eaten
    print(f'Food is enough! Leftovers: {food_left} grams.')
else:
    food_needed = grams_eaten - food_bought_grams
    print(f'Food is not enough. You need {food_needed} grams more.')
