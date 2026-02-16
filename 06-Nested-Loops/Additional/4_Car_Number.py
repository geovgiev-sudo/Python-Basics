starting_interval = int(input())
ending_interval = int(input())

for n1 in range(starting_interval, ending_interval + 1):
    for n2 in range(starting_interval, ending_interval + 1):
        for n3 in range(starting_interval, ending_interval + 1):
            for n4 in range(starting_interval, ending_interval + 1):
                if (n1 % 2 == 0 and n4 % 2 != 0) or (n1 % 2 != 0 and n4 % 2 == 0):
                    if n1 > n4:
                        if (n2 + n3) % 2 == 0:
                            print(f'{n1}{n2}{n3}{n4}', end=' ')