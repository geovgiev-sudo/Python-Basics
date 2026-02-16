chicken = 10.35
fish = 12.40
vegetarian = 8.15
delivery_cost = 2.50

number_of_chicken = int(input())
number_of_fish = int(input())
number_of_vegetarian = int(input())

price_of_chicken = number_of_chicken * chicken
price_of_fish = number_of_fish * fish
price_of_vegetarian = number_of_vegetarian * vegetarian

total_sum = price_of_chicken + price_of_fish + price_of_vegetarian

desert_price = total_sum * 0.20

total_sum_all = total_sum + delivery_cost + desert_price

print(f"{total_sum_all:.2f}")