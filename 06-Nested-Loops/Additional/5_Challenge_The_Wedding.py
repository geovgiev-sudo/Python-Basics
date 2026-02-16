men_count = int(input())
women_count = int(input())
maximum_tables = int(input())
places_taken = 0

for men in range(1, men_count + 1):
    for women in range(1, women_count + 1):
        places_taken += 2
        if places_taken > maximum_tables * 2:
            break
        print(f'({men} <-> {women})', end=' ')