bottles_of_detergent = int(input())
detergent = bottles_of_detergent * 750

ml_per_plate = 5
ml_per_pot = 15

loads_count = 0
plates_count = 0
pots_count = 0

command = input()

while command != 'End':
    load = int(command)
    loads_count += 1

    if loads_count % 3 == 0:
        detergent -= load * ml_per_pot
        pots_count += load
    else:
        detergent -= load * ml_per_plate
        plates_count += load

    if detergent < 0:
        print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
        break

    command = input()

else:
     print(f'Detergent was enough!')
     print(f'{plates_count} dishes and {pots_count} pots were washed.')
     print(f'Leftover detergent {detergent} ml.')