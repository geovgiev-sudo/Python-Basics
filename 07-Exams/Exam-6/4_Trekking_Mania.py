groups_of_climbers = int(input())
people_musala = 0
people_monblan = 0
people_kilimandjaro = 0
people_k2 = 0
people_everest = 0
people_total = 0

for i in range(1, groups_of_climbers + 1):
    people = int(input())
    people_total += people

    if people <= 5:
        people_musala += people
    elif 5 < people <= 12:
        people_monblan += people
    elif 12 < people <= 25:
        people_kilimandjaro += people
    elif 25 < people <= 40:
        people_k2 += people
    elif 41 <= people:
        people_everest += people

protzent_musala = people_musala / people_total * 100
protzent_monblan = people_monblan / people_total * 100
protzent_kilimandjaro = people_kilimandjaro / people_total * 100
protzent_k2 = people_k2 / people_total * 100
protzent_everest = people_everest / people_total * 100
print(f'{protzent_musala:.2f}%')
print(f'{protzent_monblan:.2f}%')
print(f'{protzent_kilimandjaro:.2f}%')
print(f'{protzent_k2:.2f}%')
print(f'{protzent_everest:.2f}%')