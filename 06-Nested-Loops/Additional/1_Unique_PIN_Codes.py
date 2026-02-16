first_number = int(input())
second_number = int(input())
third_number = int(input())

for number1 in range(2, first_number + 1, 2): # проверка за четни числа

    for number2 in range(2, second_number + 1):
        if number2 > 7:
            continue

        is_prime = True

        for i in range(2, number2):
            if number2 % i == 0:
                is_prime = False
                break

        if is_prime:
            for number3 in range(2, third_number + 1, 2):
                print(f'{number1} {number2} {number3}')