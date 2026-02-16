groups_of_climbers = int(input())
people_in_group = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(groups_of_climbers):
    people_in_group = int(input())
    if people_in_group <= 5:
        p1 += people_in_group
    elif 5 < people_in_group <= 12:
        p2 += people_in_group
    elif 12 < people_in_group <= 25:
        p3 += people_in_group
    elif 25 < people_in_group <= 40:
        p4 += people_in_group
    elif people_in_group >= 41:
        p5 += people_in_group

total_people = p1 + p2 + p3 + p4 + p5

print(f'{p1 / total_people * 100:.2f}%')
print(f'{p2 / total_people * 100:.2f}%')
print(f'{p3 / total_people * 100:.2f}%')
print(f'{p4 / total_people * 100:.2f}%')
print(f'{p5 / total_people * 100:.2f}%')