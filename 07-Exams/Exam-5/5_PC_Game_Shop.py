games_sold = int(input())
hearthstone_sold = 0
fornite_sold = 0
overwatch_sold = 0
other_sold = 0
total_sold = 0

for i in range(1, games_sold + 1):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone_sold += 1
        total_sold += 1
    elif game_name == 'Fornite':
        fornite_sold += 1
        total_sold += 1
    elif game_name == 'Overwatch':
        overwatch_sold += 1
        total_sold += 1
    else:
        other_sold += 1
        total_sold += 1

protzent_hearthstone = hearthstone_sold / games_sold * 100
protzent_fornite = fornite_sold / games_sold * 100
protzent_overwatch = overwatch_sold / games_sold * 100
protzent_other = other_sold / games_sold * 100

print(f'Hearthstone - {protzent_hearthstone:.2f}%')
print(f'Fornite - {protzent_fornite:.2f}%')
print(f'Overwatch - {protzent_overwatch:.2f}%')
print(f'Others - {protzent_other:.2f}%')