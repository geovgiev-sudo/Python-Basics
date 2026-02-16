film_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
kino_percentage = int(input())

income_per_day = tickets_count * ticket_price
income_period = income_per_day * days_count
kino = income_period * kino_percentage / 100
income = income_period - kino

print(f'The profit from the movie {film_name} is {income:.2f} lv.')