trunk_capacity = float(input())
command = input()
suitcase_counter = 0
suitcase_size_total = 0

while command != 'End':
    suitcase_size = float(command)

    if (suitcase_counter + 1) % 3 == 0:
        suitcase_size = suitcase_size * 1.10

    if suitcase_size >= trunk_capacity:
        print(f'No more space!')
        break

    suitcase_size_total += suitcase_size
    trunk_capacity -= suitcase_size
    suitcase_counter += 1
    command = input()

else:
    print(f'Congratulations! All suitcases are loaded!')

print(f'Statistic: {suitcase_counter} suitcases loaded.')