n = int(input())
count = 0

for i in range(n):
    number = int(input())
    count += number

average = count / n
print(f'{average:.2f}')