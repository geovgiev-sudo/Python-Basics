voucher_value = int(input())
command = input()

ticket_counter = 0
buy_counter_tickets = 0
buy_counter_products = 0
price = 0

while command != 'End':
    buy = command

    if len(buy) > 8:
        price = ord(buy[0]) + ord(buy[1])
        if voucher_value >= price:
            voucher_value -= price
            buy_counter_tickets += 1
        else:
            break

    elif len(buy) <= 8:
        price = ord(buy[0])
        if voucher_value >= price:
            voucher_value -= price
            buy_counter_products += 1
        else:
            break

    command = input()

print(f'{buy_counter_tickets}')
print(f'{buy_counter_products}')