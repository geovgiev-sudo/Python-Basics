eggs_quantity = int(input())
command = input()
buy_counter = 0

while command != 'Close':
    action = command

    if action == 'Buy':
        eggs_buy = int(input())
        if eggs_quantity < eggs_buy:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {eggs_quantity}.')
            break
        buy_counter += eggs_buy
        eggs_quantity -= eggs_buy

    elif action == 'Fill':
        eggs_fill = int(input())
        eggs_quantity += eggs_fill

    command = input()

else:
    print(f'Store is closed!')
    print(f'{buy_counter} eggs sold.')