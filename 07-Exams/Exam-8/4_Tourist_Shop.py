budget = float(input())
budget_left = 0
products_bought = 0
products_price_total = 0
command = input()

while command != 'Stop':
    product_name = command
    product_price = float(input())
    products_bought += 1

    if products_bought % 3 == 0:
        product_price /= 2

    budget_left = budget - products_price_total

    if product_price > budget_left:
        print(f'You don\'t have enough money!')
        money_needed = product_price - budget_left
        print(f'You need {money_needed:.2f} leva!')
        break

    products_price_total += product_price
    command = input()

else:
    print(f'You bought {products_bought} products for {products_price_total:.2f} leva.')