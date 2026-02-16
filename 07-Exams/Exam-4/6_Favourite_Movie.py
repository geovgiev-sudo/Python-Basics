import sys
command = input()
film_counter = 0
film_sum_max = -sys.maxsize
best_film = ''

while command != 'STOP':
    film_counter += 1
    if film_counter == 7:
        print(f'The limit is reached.')
        break

    film_title = command
    film_title_length = len(film_title)
    film_sum = 0

    for symbol in film_title:
        film_sum += ord(symbol)

        if 97 <= ord(symbol) <= 122:
            film_sum -= 2 * film_title_length
        elif 65 <= ord(symbol) <= 90:
            film_sum -= film_title_length

    if film_sum > film_sum_max:
        film_sum_max = film_sum
        best_film = film_title

    command = input()

print(f'The best movie for you is {best_film} with {film_sum_max} ASCII sum.')

# small_ascii - 97 - 122
# big_ascii - 65 - 90