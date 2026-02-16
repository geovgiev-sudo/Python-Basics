animal = input()
tip = ''

if animal == 'dog':
    tip = 'mammal'
elif ((animal == 'crocodile')
        or (animal == 'tortoise')
        or (animal == 'snake')):
    tip = 'reptile'
else:
    tip = 'unknown'
print(tip)
