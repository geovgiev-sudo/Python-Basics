days = int(input())
booking = input()
grade = input()

nights = days - 1
price_night = 0
price = 0

if booking == 'room for one person':
    price_night = 18
    price = nights * price_night

elif booking == 'apartment':
    price_night = 25
    price = nights * price_night
    if days < 10:
        price *= 0.70
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.50

elif booking == 'president apartment':
    price_night = 35
    price = nights * price_night
    if days < 10:
        price *= 0.90
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.80

if grade == 'positive':
    price *= 1.25
elif grade == 'negative':
    price *= 0.90

print(f'{price:.2f}')