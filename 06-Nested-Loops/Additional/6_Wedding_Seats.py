last_sector = input()
rows_sector_A = int(input())
odd_row_places = int(input())
total_places = 0
last_sector_digit = ord(last_sector)

for sector in range(ord('A'), last_sector_digit + 1):
    current_rows = rows_sector_A + (sector - ord('A'))

    for row in range(1, current_rows + 1):

        if row % 2 == 0:
            current_places_count = odd_row_places + 2

        else:
            current_places_count = odd_row_places

        for place in range(ord('a'), ord('a') + current_places_count):
            print(f'{chr(sector)}{row}{chr(place)}')
            total_places += 1

print(f'{total_places}')

