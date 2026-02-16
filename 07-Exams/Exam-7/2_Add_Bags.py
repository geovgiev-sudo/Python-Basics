luggage_over_20 = float(input())
kg_luggage = float(input())
travel_days = int(input())
number_of_luggage = int(input())
luggage_price = 0

if kg_luggage < 10:
    luggage_price = luggage_over_20 * 0.20
elif 10 <= kg_luggage <= 20:
    luggage_price = luggage_over_20 * 0.50
elif 20 < kg_luggage:
    luggage_price = luggage_over_20

if travel_days > 30:
    luggage_price *= 1.10
elif 7 <= travel_days <= 30:
    luggage_price *= 1.15
elif travel_days < 7:
    luggage_price *= 1.40

total_luggage = number_of_luggage * luggage_price
print(f'The total price of bags is: {total_luggage:.2f} lv.')