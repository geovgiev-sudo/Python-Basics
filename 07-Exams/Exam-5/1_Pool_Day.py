from math import ceil

number_of_people = int(input())
entrance_fee = float(input())
shezlong_price = float(input())
umbrella_price = float(input())

entrance_total = number_of_people * entrance_fee
number_of_shezlong = ceil(number_of_people * 0.75)
shezlong_total = shezlong_price * number_of_shezlong
number_of_umbrellas = ceil(number_of_people * 0.50)
umbrella_total = number_of_umbrellas * umbrella_price

total_price = entrance_total + shezlong_total + umbrella_total
print(f'{total_price:.2f} lv.')