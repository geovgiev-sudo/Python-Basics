yearly_tax = int(input())

ketzove_price = yearly_tax * (1 - 0.40) # метод за изчисляване на отстъпка
ekip_price = ketzove_price * (1 - 0.20) # метод за изчисляване на отстъпка
ball_price = ekip_price / 4
accessories_price = ball_price / 5

total_price = yearly_tax + ketzove_price + ekip_price + ball_price + accessories_price
print(f"{total_price:.2f}")

print(f"{ketzove_price:.2f}")
print(f"{ekip_price:.2f}")
print(f"{ball_price:.2f}")
print(f"{accessories_price:.2f}")