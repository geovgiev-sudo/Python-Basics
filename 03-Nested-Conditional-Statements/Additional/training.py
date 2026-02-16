number = int(input())

# Вземаме отделните цифри, но в обратен ред
third_digit = number // 100          # стотици
second_digit = (number // 10) % 10   # десетици
first_digit = number % 10            # единици

# обръщаме реда (1 -> трета цифра и т.н.)
a = first_digit
b = second_digit
c = third_digit

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            result = i * j * k
            print(f"{i} * {j} * {k} = {result};")