piece_width = 1
piece_length = 1

cake_width = int(input())
cake_length = int(input())
cake_size = cake_width * cake_length # парчета торта --> 1cm * 1 cm
pieces_taken = 0

command = input()

while command != 'STOP':
    piece = int(command)
    pieces_taken += piece

    if cake_size < pieces_taken:
        break

    command = input()

if command == 'Stop' or cake_size < pieces_taken:
    pieces_more = pieces_taken - cake_size
    print(f'No more cake left! You need {pieces_more} pieces more.')

elif cake_size >= pieces_taken:
    pieces_left = cake_size - pieces_taken
    print(f'{pieces_left} pieces are left.')