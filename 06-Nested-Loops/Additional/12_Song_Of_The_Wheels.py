m = int(input())
combinations_count = 0
password = ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b) and (c > d) and (a * b + c * d) == m:
                    print(f'{a}{b}{c}{d}', end=' ')

                    combinations_count += 1

                    if combinations_count == 4:
                        password = f'{a}{b}{c}{d}'

print()

if password != '':
    print(f'Password: {password}')
else:
    print(f'No!')
