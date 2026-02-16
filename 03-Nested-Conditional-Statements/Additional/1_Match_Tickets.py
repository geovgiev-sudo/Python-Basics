budget = float(input())
category = input()
people = int(input())

vip_price = 499.99
normal_price = 249.99

transport_price = 0
tickets_price = 0

if 1 <= people <= 4:
    transport_price = budget * 0.75

elif 5 <= people <= 9:
    transport_price = budget * 0.60

elif 10 <= people <= 24:
    transport_price = budget * 0.50

elif 25 <= people <= 49:
    transport_price = budget * 0.40

elif people > 50:
    transport_price = budget * 0.25

if category == 'Normal':
        tickets_price = people * normal_price
elif category == 'VIP':
        tickets_price = people * vip_price

total_costs = transport_price + tickets_price

if budget >= total_costs:
    money_left = budget - total_costs
    print(f'Yes! You have {money_left:.2f} leva left.')
elif budget < total_costs:
    money_needed = total_costs - budget
    print (f'Not enough money! You need {money_needed:.2f} leva.')