import sys

sys.setrecursionlimit(2000)

starting_letter = input()
ending_letter = input()
missing_letter = input()
valid_combinations = 0

start_code = ord(starting_letter)
end_code = ord(ending_letter)

for code1 in range(start_code, end_code + 1):
    letter1 = chr(code1)
    for code2 in range(start_code, end_code + 1):
        letter2 = chr(code2)
        for code3 in range(start_code, end_code + 1):
            letter3 = chr(code3)

            if letter1 != missing_letter and letter2 != missing_letter and letter3 != missing_letter:
                combination = letter1 + letter2 + letter3
                valid_combinations += 1
                print(f'{combination}', end=' ')

print(valid_combinations)