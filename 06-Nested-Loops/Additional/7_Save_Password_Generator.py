# Четене на входните данни
try:
    a = int(input())
    b = int(input())
    max_passwords = int(input())
except EOFError:
    exit()

# Инициализация
passwords_count = 0
output_string = ""

# А (i) и B (j) започват от минималните си стойности
i = 35  # Първо А
j = 64  # Първо Б

# 1. Цикъл за x (k): от 1 до a
for k in range(1, a + 1):

    # 2. Цикъл за y (l): от 1 до b
    for l in range(1, b + 1):

        # 3. Проверка за лимит
        if passwords_count >= max_passwords:
            break

        # 4. Генериране на Паролата

        # Символ 1 (A): chr(i)
        # Символ 2 (B): chr(j)
        # Символ 3 (x): str(k)
        # Символ 4 (y): str(l)
        # Символ 5 (B): chr(j)
        # Символ 6 (A): chr(i)

        password = (
                chr(i) +
                chr(j) +
                str(k) +
                str(l) +
                chr(j) +  # Второто B е равно на първото B
                chr(i)  # Второто A е равно на първото A
        )

        output_string += password + "|"
        passwords_count += 1

        # 5. Прилагане на ПРАВИЛАТА ЗА УВЕЛИЧАВАНЕ (ВСИЧКИ СЕ УВЕЛИЧАВАТ ВЕДНЪЖ)

        # Увеличаване на i (A)
        i += 1
        # Правило за A: Ако надхвърли 55, връща се на 35
        if i > 55:
            i = 35

        # Увеличаване на j (B)
        j += 1
        # Правило за B: Ако надхвърли 96, връща се на 64
        if j > 96:
            j = 64

    if passwords_count >= max_passwords:
        break

# 6. Финален Изход
if output_string:
    final_output = output_string  # Премахване на последния '|'
    print(final_output)
else:
    print("")