eggs_size = input()
eggs_colour = input()
number_of_partidas = int(input())
price_per_partida = 0

if eggs_size == 'Large':
    if eggs_colour == 'Red':
        price_per_partida = 16
    elif eggs_colour == 'Green':
        price_per_partida = 12
    elif eggs_colour == 'Yellow':
        price_per_partida = 9

if eggs_size == 'Medium':
    if eggs_colour == 'Red':
        price_per_partida = 13
    elif eggs_colour == 'Green':
        price_per_partida = 9
    elif eggs_colour == 'Yellow':
        price_per_partida = 7

if eggs_size == 'Small':
    if eggs_colour == 'Red':
        price_per_partida = 9
    elif eggs_colour == 'Green':
        price_per_partida = 8
    elif eggs_colour == 'Yellow':
        price_per_partida = 5

price = number_of_partidas * price_per_partida
expenses = price * 35 / 100
revenue = price - expenses

print(f'{revenue:.2f} leva.')