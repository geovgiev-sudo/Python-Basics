first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0

    for index, char_digit in enumerate(number_to_str): # enumerate прави кортеж (tuple)
        # index e позицията, digit e самото число КАТО СТРИНГ
        if index % 2 == 0:
            even_sum += int(char_digit) # понеже digit e стринг,
            # тук го превръщаме в интегер, за да можем да правим math shit
        else:
            odd_sum += int(char_digit)

    if even_sum == odd_sum:
        print(number, end= ' ')


start_interval = int(input())
end_interval = int(input())

for number in range(start_interval, end_interval + 1):
    even_sum = 0
    odd_sum = 0
    position = 0
    number = str(number)
    for symbol in number:
        if position % 2 == 0:
            even_sum += int(symbol)
        else:
            odd_sum += int(symbol)

        position += 1

    if even_sum == odd_sum:
        print(number, end=' ')


start_interval = int(input())
end_interval = int(input())

for number in range(start_interval, end_interval + 1):
    number_str = str(number)
    even_sum = 0
    odd_sum = 0

    for position in range(6): # Няма смисъл да е 1, 7, защото
        digit = int(number_str[position]) # Стринговете винаги започват от 0

        if (position + 1) % 2 == 0: # Слагам + 1 - Питам това първа, втора, трета цифра ли е, не мога да питам "това нулев знак ли е"
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(number, end=' ')