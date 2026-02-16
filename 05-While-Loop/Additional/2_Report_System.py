expected_sum = int(input())

card_pays = 0
card_pays_sum = 0
cash_pays = 0
cash_pays_sum = 0
product_price = 0
transaction_number = 1
gathered_sum = 0

command = input()

while command != 'End':
    product_price = int(command)

    if transaction_number % 2 != 0:
        if product_price > 100:
            print(f'Error in transaction!')
        else:
            gathered_sum += product_price
            cash_pays_sum += product_price
            cash_pays += 1
            print(f'Product sold!')
    else:
        if product_price < 10:
            print(f'Error in transaction!')
        else:
            gathered_sum += product_price
            card_pays_sum += product_price
            card_pays += 1
            print(f'Product sold!')

    if gathered_sum >= expected_sum:
        average_cash = cash_pays_sum / cash_pays
        average_card = card_pays_sum / card_pays
        print(f'Average CS: {average_cash:.2f}')
        print(f'Average CC: {average_card:.2f}')
        break

    transaction_number += 1
    command = input()

else:
    print('Failed to collect required money for charity.')