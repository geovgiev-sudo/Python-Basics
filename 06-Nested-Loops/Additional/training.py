import sys
# Увеличете лимита за рекурсия, ако е необходимо, но тук не е нужно
# sys.setrecursionlimit(2000)

starting_letter = input()
ending_letter = input()
missing_letter = input()
valid_combinations = 0

# Получаваме ASCII стойностите за началото и края на интервала
start_code = ord(starting_letter)
end_code = ord(ending_letter)

# Итерираме през всички букви в интервала (включително крайната)
# за всяка от трите позиции в комбинацията

for code1 in range(start_code, end_code + 1):
    letter1 = chr(code1)
    for code2 in range(start_code, end_code + 1):
        letter2 = chr(code2)
        for code3 in range(start_code, end_code + 1):
            letter3 = chr(code3)

            # Проверяваме дали някоя от буквите съдържа пропуснатата буква
            if letter1 != missing_letter and letter2 != missing_letter and letter3 != missing_letter:
                combination = letter1 + letter2 + letter3
                valid_combinations += 1
                print(f'{combination}', end=' ')

# След като всички комбинации са отпечатани, отпечатваме броя им на нов ред
print(valid_combinations)