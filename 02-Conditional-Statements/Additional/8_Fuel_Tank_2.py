gasoline_per_litre = 2.22
diesel_per_litre = 2.33
gas_per_litre = 0.93

fuel_type = input()
fuel_litres = float(input())
club_cart = input()

price_per_litre = 0

if fuel_type == 'Gasoline':
    price_per_litre = gasoline_per_litre
    if club_cart == 'Yes':
        price_per_litre -= 0.18
elif fuel_type == 'Diesel':
    price_per_litre = diesel_per_litre
    if club_cart == 'Yes':
        price_per_litre -= 0.12
elif fuel_type == 'Gas':
    price_per_litre = gas_per_litre
    if club_cart == 'Yes':
        price_per_litre -= 0.08

total_price = price_per_litre * fuel_litres

if 20 <= fuel_litres <= 25:
    total_price *= 0.92
elif fuel_litres > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")