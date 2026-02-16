metri = float(input())
price_per_meter = 7.61

total = metri * price_per_meter

discount = 0.18 * total
total_discount = total - discount

print(f"The final price is: {total_discount:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")