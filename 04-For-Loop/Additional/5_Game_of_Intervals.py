turns = int(input())
result = 0

count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
count_invalid = 0

for num in range(1, turns + 1):
    number = int(input())
    if 0 <= number <= 9:
        count_0_9 += 1
        result += number * 0.20
    elif 10 <= number <= 19:
        count_10_19 += 1
        result += number * 0.30
    elif 20 <= number <= 29:
        count_20_29 += 1
        result += number * 0.40
    elif 30 <= number <= 39:
        count_30_39 += 1
        result += 50
    elif 40 <= number <= 50:
        count_40_50 += 1
        result += 100
    else:
        count_invalid += 1
        result /= 2

total_count = (count_0_9 + count_10_19 + count_20_29
               + count_30_39 + count_40_50 + count_invalid)

c1_percent = f'{count_0_9 / turns * 100:.2f}%'
c2_percent = f'{count_10_19 / turns * 100:.2f}%'
c3_percent = f'{count_20_29 / turns * 100:.2f}%'
c4_percent = f'{count_30_39 / turns * 100:.2f}%'
c5_percent = f'{count_40_50 / turns * 100:.2f}%'
c_invalid_percent = f'{count_invalid / turns * 100:.2f}%'

print(f'{result:.2f}')
print(f'From 0 to 9: {c1_percent}')
print(f'From 10 to 19: {c2_percent}')
print(f'From 20 to 29: {c3_percent}')
print(f'From 30 to 39: {c4_percent}')
print(f'From 40 to 50: {c5_percent}')
print(f'Invalid numbers: {c_invalid_percent}')