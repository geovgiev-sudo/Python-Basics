g = int(input())
time = input()
outfit = ''
shoes = ''

if time == 'Morning':
    if 10 <= g <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < g <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif g >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time == 'Afternoon':
    if 10 <= g <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < g <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif g >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif time == 'Evening':
    if 10 <= g <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < g <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif g >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {g} degrees, get your {outfit} and {shoes}.")

