first_pair = int(input())
second_pair = int(input())
difference_first_pair = int(input())
difference_second_pair = int(input())

value_max1 = first_pair + difference_first_pair
value_max2 = second_pair + difference_second_pair

for d1 in range(first_pair, value_max1 + 1):

    is_prime1 = True
    for i in range(2, int(d1 ** 0.5) + 1):
        if d1 % i == 0:
            is_prime1 = False
            break

    for d2 in range(second_pair, value_max2 + 1):

        is_prime2 = True

        for j in range(2, int(d2 ** 0.5) + 1):
            if d2 % j == 0:
                is_prime2 = False
                break

        if is_prime1 and is_prime2:
            print(f'{d1}{d2}')