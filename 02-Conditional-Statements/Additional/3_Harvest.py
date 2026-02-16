from math import floor, ceil

loze_area = int(input())
grozde_per_metre = float(input())
wine_to_sell = int(input())
workers = int(input())

rekolta = loze_area * grozde_per_metre
produced_wine = rekolta * 0.40 / 2.5
difference = abs(produced_wine - wine_to_sell)
wine_per_worker = difference / workers

if produced_wine < wine_to_sell:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
elif produced_wine >= wine_to_sell:
    print(f'Good harvest this year! Total wine: {ceil(produced_wine)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.')
