salle_capacity = int(input())
ticket_price = 5
people_count = 0
entrance_price = 0
income = 0
command = input()

while command != 'Movie time!':
    people = int(command)
    people_count += people

    if people_count > salle_capacity:
        print(f'The cinema is full.')
        print(f'Cinema income - {income} lv.')
        break

    entrance_price = people * ticket_price

    if people % 3 == 0:
        entrance_price = ticket_price * people - 5

    income += entrance_price

    command = input()

else:
    print(f'There are {salle_capacity - people_count} seats left in the cinema.')
    print(f'Cinema income - {income} lv.')