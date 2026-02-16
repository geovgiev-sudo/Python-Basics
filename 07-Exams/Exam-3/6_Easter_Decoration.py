basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7
total_purchases = 0

number_of_clients = int(input())

for i in range(1, number_of_clients + 1):
    command = input()
    current_purchase = 0
    basket_count = 0
    wreath_count = 0
    chocolate_bunny_count = 0

    while command != 'Finish':
        purchase = command
        current_purchase += 1

        if purchase == 'basket':
            basket_count += 1
        elif purchase == 'wreath':
            wreath_count += 1
        elif purchase == 'chocolate bunny':
            chocolate_bunny_count += 1

        command = input()

    current_basket_total = basket_count * basket_price
    current_wreath_total = wreath_count * wreath_price
    current_choco_total = chocolate_bunny_count * chocolate_bunny_price
    current_total = current_basket_total + current_wreath_total + current_choco_total
    if current_purchase % 2 == 0:
        current_total *= 0.80
    total_purchases += current_total
    print(f'You purchased {current_purchase} items for {current_total:.2f} leva.')
average = total_purchases / number_of_clients
print(f'Average bill per client is: {average:.2f} leva.')