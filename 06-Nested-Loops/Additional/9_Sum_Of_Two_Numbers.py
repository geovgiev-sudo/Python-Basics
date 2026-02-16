start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combinations_count = 0

for d1 in range(start_interval, end_interval + 1):
    for d2 in range(start_interval, end_interval + 1):
        combinations_count += 1
        if d1 + d2 == magic_number:
            print(f'Combination N:{combinations_count} ({d1} + {d2} = {magic_number})')
            exit()

print(f'{combinations_count} combinations - neither equals {magic_number}')