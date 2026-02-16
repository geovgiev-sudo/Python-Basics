import sys

number_of_films = int(input())
max_rating = -sys.maxsize
min_rating = sys.maxsize
max_rating_film = ''
min_rating_film = ''
ratings_count = 0

for i in range(1, number_of_films + 1):
    film_name = input()
    film_rating = float(input())
    ratings_count += film_rating
    if film_rating > max_rating:
        max_rating = film_rating
        max_rating_film = film_name
    if film_rating < min_rating:
        min_rating = film_rating
        min_rating_film = film_name

average_rating = ratings_count / number_of_films

print(f'{max_rating_film} is with highest rating: {max_rating:.1f}')
print(f'{min_rating_film} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')