budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
protzent_extra = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95

nights_price = number_of_nights * price_per_night
extra = budget * (protzent_extra / 100)
total_sum = nights_price + extra

if total_sum <= budget:
    money_left = budget - total_sum
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')

elif total_sum > budget:
    money_needed = total_sum - budget
    print(f'{money_needed:.2f} leva needed.')