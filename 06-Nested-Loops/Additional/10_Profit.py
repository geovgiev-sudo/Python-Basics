moneti_1lv = int(input())
moneti_2lv = int(input())
banknoti_5lv = int(input())
total_sum = int(input())

for i in range(moneti_1lv + 1):
    for j in range(moneti_2lv + 1):
        for k in range(banknoti_5lv + 1):
            lev = i * 1
            lev2 = j * 2
            lev5 = k * 5
            if lev + lev2 + lev5 == total_sum:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {total_sum} lv.')