a1 = int(input())
a2 = int(input())
n = int(input())
d3_n = n / 2

for symbol1 in range(a1, a2):
    symbol1_str = chr(symbol1)

    for d2 in range(1, n):

        for d3 in range(1, int(n / 2)):

            d4 = symbol1

            if symbol1 % 2 != 0 and (d2 + d3 + d4) % 2 != 0:
                print(f'{symbol1_str}-{d2}{d3}{d4}')