hundreds_limit = int(input())
tens_limit = int(input())
ones_limit = int(input())

for d1 in range(2, hundreds_limit + 1, 2):

    for d2 in range(2, tens_limit + 1):
        if d2 > 7:
            continue

        is_prime = True

        for i in range(2, d2):
            if d2 % i == 0:
                is_prime = False
                break

        if is_prime:
            for d3 in range(2, ones_limit + 1, 2):
                print(f'{d1} {d2} {d3}')