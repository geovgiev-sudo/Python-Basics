hour = int(input())
minutes = int(input())

total_minutes = (hour * 60) + minutes + 15

new_hour = (total_minutes // 60) % 24 # Изчисляваме новия час, но тъй като трябва да има 0, правим деление с остатък (питаме колко пъти се побира 24 в 24 и какъв е остатъкът)
new_minutes = total_minutes % 60

print(f'{new_hour}:{new_minutes:02d}')