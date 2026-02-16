n = int(input()) # 3
left_sum = 0
right_sum = 0

for idx in range(n * 2): # 0, 1, 2, 3, 4, 5
    new_number = int(input())

    if idx < n:
        left_sum += new_number
    else:
        right_sum += new_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')