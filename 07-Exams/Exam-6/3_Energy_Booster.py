fruit = input()
set_size = input()
set_count = int(input())
price = 0
order_price = 0
if set_size == 'small':
    if fruit == 'Watermelon':
        price = 56 * 2
    elif fruit == 'Mango':
        price = 36.66 * 2
    elif fruit == 'Pineapple':
        price = 42.10 * 2
    elif fruit == 'Raspberry':
        price = 20 * 2
elif set_size == 'big':
    if fruit == 'Watermelon':
        price = 28.70 * 5
    elif fruit == 'Mango':
        price = 19.60 * 5
    elif fruit == 'Pineapple':
        price = 24.80 * 5
    elif fruit == 'Raspberry':
        price = 15.20 * 5

order_price = set_count * price

if 400 <= order_price <= 1000:
    order_price = order_price * 0.85
elif order_price > 1000:
    order_price = order_price * 0.50

print(f'{order_price:.2f} lv.')