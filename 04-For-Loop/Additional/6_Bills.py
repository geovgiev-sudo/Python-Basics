months = int(input())
electricity = 0
water = 0
internet = 0
monthly_other = 0
other = 0

for i in range(1, months + 1):
    current_electricity = float(input())
    electricity += current_electricity
    water += 20
    internet += 15
    monthly_other = (current_electricity + 20 + 15) * 1.20
    other += monthly_other

total_expenses = electricity + water + internet + other
average_expenses = total_expenses/months

print (f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average_expenses:.2f} lv')