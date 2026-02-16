starting_interval = int(input())
starting_interval_str = str(starting_interval)
ending_interval = int(input())
ending_interval_real = ending_interval
ending_interval_str = str(ending_interval_real)

for d1 in range(int(starting_interval_str[0]), int(ending_interval_str[0]) + 1):
    for d2 in range(int(starting_interval_str[1]), int(ending_interval_str[1]) + 1):
        for d3 in range(int(starting_interval_str[2]), int(ending_interval_str[2]) + 1):
            for d4 in range(int(starting_interval_str[3]), int(ending_interval_str[3]) + 1):
                if d1 % 2 != 0 and d2 % 2 != 0 and d3 % 2 != 0 and d4 % 2 != 0:
                    print(f'{d1}{d2}{d3}{d4}', end=' ')
