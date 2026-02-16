film_name = input()
room_type = input()
tickets_bought = int(input())
ticket_price = 0

if film_name == 'A Star Is Born':
    if room_type == 'normal':
        ticket_price = 7.50
    elif room_type == 'luxury':
        ticket_price = 10.50
    elif room_type == 'ultra luxury':
        ticket_price = 13.50

if film_name == 'Bohemian Rhapsody':
    if room_type == 'normal':
        ticket_price = 7.35
    elif room_type == 'luxury':
        ticket_price = 9.45
    elif room_type == 'ultra luxury':
        ticket_price = 12.75

if film_name == 'Green Book':
    if room_type == 'normal':
        ticket_price = 8.15
    elif room_type == 'luxury':
        ticket_price = 10.25
    elif room_type == 'ultra luxury':
        ticket_price = 13.25

if film_name == 'The Favourite':
    if room_type == 'normal':
        ticket_price = 8.75
    elif room_type == 'luxury':
        ticket_price = 11.55
    elif room_type == 'ultra luxury':
        ticket_price = 13.95

prihodi = tickets_bought * ticket_price

print(f'{film_name} -> {prihodi:.2f} lv.')