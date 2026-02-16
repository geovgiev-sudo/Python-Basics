price_per_pen = 5.80
price_per_marker = 7.20
price_per_litre = 1.20

number_of_pens = int(input())
number_of_markers = int(input())
litres_preparat = int(input())
discount_protzent = int(input())

price_of_pens = number_of_pens * price_per_pen
price_of_markers = number_of_markers * price_per_marker
price_of_preparat = litres_preparat * price_per_litre

total_price = price_of_pens + price_of_markers + price_of_preparat

discount = total_price * discount_protzent / 100
price_with_discount = total_price - discount

print(price_with_discount)
