n = int(input()) # 4
sum_numbers = 0

for _ in range(n): # 0, 1, 2, 3
    new_number = int(input()) # Чрез for цикъл викаме input функцията
    sum_numbers += new_number # sum_numbers + new_number

print(sum_numbers)