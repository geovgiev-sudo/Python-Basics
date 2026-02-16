strawberry_price_kg = float(input())
banana_kg = float(input())
orange_kg = float(input())
malini_kg = float(input())
strawberry_kg = float(input())

malini_price_kg = strawberry_price_kg * 0.50
orange_price_kg = malini_price_kg * 0.60
banana_price_kg = malini_price_kg - (malini_price_kg * 80 / 100)

strawberry_price = strawberry_price_kg * strawberry_kg
banana_price = banana_price_kg * banana_kg
orange_price = orange_price_kg * orange_kg
malini_price = malini_price_kg * malini_kg

total_price = strawberry_price + banana_price + orange_price + malini_price

print(f'{total_price:.2f}')
