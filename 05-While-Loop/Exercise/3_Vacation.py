needed_money = float(input())
available_sum = float(input())

days = 0
consecutive_spends_days = 0

while available_sum < needed_money and consecutive_spends_days < 5:
    action = input()
    amount = float(input())
    days += 1

    if action == 'spend':
        available_sum -= amount
        if available_sum < 0:
            available_sum = 0
        consecutive_spends_days += 1

    elif action == 'save':
        available_sum += amount
        consecutive_spends_days = 0

if consecutive_spends_days == 5:
    print('You can\'t save the money.')
    print(f'{days}')
else:
    print(f'You saved the money for {days} days.')