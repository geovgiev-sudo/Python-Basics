veggie_price_per_kg = float(input())
fruit_price_per_kg = float(input())
veggie_total_kg = int(input())
fruit_total_kg = int(input())

veggie_price_lv = veggie_price_per_kg * veggie_total_kg
fruit_price_lv = fruit_price_per_kg * fruit_total_kg

total_price_lv = veggie_price_lv + fruit_price_lv
total_price_eur = total_price_lv / 1.94
print(f"{total_price_eur:.2f}")