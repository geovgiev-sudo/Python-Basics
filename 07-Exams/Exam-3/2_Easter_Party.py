number_of_guests = int(input())
kuvert_per_person = float(input())
budget = float(input())
cake_price = budget * 0.10
new_budget = budget - cake_price

if 10 <= number_of_guests <= 15:
    kuvert_per_person *= 0.85

elif 15 < number_of_guests <= 20:
    kuvert_per_person *= 0.80

elif number_of_guests > 20:
    kuvert_per_person *= 0.75

total_sum = number_of_guests * kuvert_per_person + cake_price

if budget >= total_sum:
    money_left = budget - total_sum
    print(f'It is party time! {money_left:.2f} leva left.')

elif budget < total_sum:
    money_needed = total_sum - budget
    print(f'No party! {money_needed:.2f} leva needed.')