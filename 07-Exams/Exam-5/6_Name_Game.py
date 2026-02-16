import sys
command = input()
max_points = -sys.maxsize
winner_name = ''
winner_points = 0

while command != 'Stop':
    player_name = command
    player_points = 0

    for letter in player_name:
        letter_ascii = ord(letter)

        # ИЛИ for letter in range(len(player_name)):
        # ИЛИ letter_ascii = ord(player_name[letter])

        # ИЛИ for index, char_digit in enumerate(player_name):
        # ИЛИ letter_ascii = ord(char_digit)

        number = int(input())

        if number == letter_ascii:
            player_points += 10
        else:
            player_points += 2

    if player_points >= max_points:
        max_points = player_points
        winner_points = max_points
        winner_name = player_name

    command = input()

print(f'The winner is {winner_name} with {winner_points} points!')