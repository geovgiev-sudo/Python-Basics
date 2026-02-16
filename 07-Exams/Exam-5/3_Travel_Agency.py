town_name = input()
package_type = input()
vip = input()
days = int(input())

if days < 1:
    print(f'Days must be positive number!')
    exit()

price_per_day = 0
protzent_vip = 0

if town_name in ['Bansko', 'Borovets']:
    if package_type == 'withEquipment':
        price_per_day = 100
        protzent_vip = 10
    elif package_type == 'noEquipment':
        price_per_day = 80
        protzent_vip = 5
    else:
        print("Invalid input!")
        exit()

elif town_name in ['Varna', 'Burgas']:
    if package_type == 'withBreakfast':
        price_per_day = 130
        protzent_vip = 12
    elif package_type == 'noBreakfast':
        price_per_day = 100
        protzent_vip = 7
    else:
        print("Invalid input!")
        exit()

else:
    print(f'Invalid input!')
    exit()

if vip == 'yes':
    price_per_day -= price_per_day * (protzent_vip / 100)

if days > 7:
    days -= 1

total_price = price_per_day * days
print(f'The price is {total_price:.2f}lv! Have a nice time!')