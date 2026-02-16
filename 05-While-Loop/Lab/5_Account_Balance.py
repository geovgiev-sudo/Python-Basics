new_input = input()
total_money = 0

while new_input != 'NoMoreMoney':
    amount = float(new_input)
    if amount < 0:
        print(f'Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')
    total_money += amount
    new_input = input()

print(f'Total: {total_money:.2f}')