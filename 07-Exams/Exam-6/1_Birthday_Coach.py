rent = float(input())
cake = rent * 0.20
beverages = cake - cake * 0.45
animator = rent / 3

money = rent + cake + beverages + animator
print(f'{money:.1f}')