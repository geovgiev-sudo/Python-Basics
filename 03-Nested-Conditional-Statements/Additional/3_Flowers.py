hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

hrizantemi_price = 0
roses_price = 0
tulips_price = 0
bouquet_price = 0

if season == 'Spring' or season == 'Summer':
    hrizantemi_price = 2
    roses_price = 4.10
    tulips_price = 2.50

elif season == 'Autumn' or season == 'Winter':
    hrizantemi_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

if holiday == 'Y':
    hrizantemi_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15
    bouquet_price = (hrizantemi * hrizantemi_price
                     + roses * roses_price +
                     tulips * tulips_price)

elif holiday == 'N':
    bouquet_price = (hrizantemi * hrizantemi_price
                     + roses * roses_price +
                     tulips * tulips_price)

if tulips > 7 and season == 'Spring':
    bouquet_price *= 0.95

if roses >= 10 and season == 'Winter':
    bouquet_price *= 0.90

if hrizantemi + roses + tulips > 20:
    bouquet_price *= 0.80

print(f'{(bouquet_price + 2):.2f}')