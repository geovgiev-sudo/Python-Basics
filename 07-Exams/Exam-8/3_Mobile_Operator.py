contract_duration = input()
contract_type = input()
mobile_internet = input()
months_to_pay = int(input())

monthly_fee = 0

if contract_duration == 'one':
    if contract_type == 'Small':
        monthly_fee = 9.98
    elif contract_type == 'Middle':
        monthly_fee = 18.99
    elif contract_type == 'Large':
        monthly_fee = 25.98
    elif contract_type == 'ExtraLarge':
        monthly_fee = 35.99

elif contract_duration == 'two':
    if contract_type == 'Small':
        monthly_fee = 8.58
    elif contract_type == 'Middle':
        monthly_fee = 17.09
    elif contract_type == 'Large':
        monthly_fee = 23.59
    elif contract_type == 'ExtraLarge':
        monthly_fee = 31.79

if mobile_internet == 'yes':
    if monthly_fee <= 10:
        monthly_fee += 5.50
    elif 10 < monthly_fee <= 30:
        monthly_fee += 4.35
    elif 30 < monthly_fee:
        monthly_fee += 3.85

if contract_duration == 'two':
    monthly_fee *= 0.9625

total_fee = monthly_fee * months_to_pay
print(f'{total_fee:.2f} lv.')