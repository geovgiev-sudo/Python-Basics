from math import ceil, floor

magnolia = 3.25
zumbul = 4
rose = 3.50
cactus = 8

magnolias = int(input())
zumbuls = int(input())
roses = int(input())
cactuss = int(input())
gift_price = float(input())

total_gain = magnolia * magnolias + zumbul * zumbuls + rose * roses + cactus * cactuss
tax = total_gain * 0.05
gain_after_tax = total_gain - tax
difference = abs(gift_price - gain_after_tax)

if gift_price <= gain_after_tax:
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(difference)} leva.')