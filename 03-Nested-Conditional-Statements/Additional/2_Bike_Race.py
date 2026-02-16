juniors = int(input())
seniors = int(input())
trace = input()

juniors_tax = 0
seniors_tax = 0
total_tax = 0

if trace == 'trail':
    juniors_tax = 5.50
    seniors_tax = 7
    total_tax = juniors * juniors_tax + seniors * seniors_tax

elif trace == 'cross-country':
    juniors_tax = 8
    seniors_tax = 9.50
    total_tax = juniors * juniors_tax + seniors * seniors_tax
    if (juniors + seniors) >= 50:
        total_tax = (juniors * juniors_tax + seniors * seniors_tax) * 0.75

elif trace == 'downhill':
    juniors_tax = 12.25
    seniors_tax = 13.75
    total_tax = juniors * juniors_tax + seniors * seniors_tax

elif trace == 'road':
    juniors_tax = 20
    seniors_tax = 21.50
    total_tax = juniors * juniors_tax + seniors * seniors_tax

expenses = total_tax * 0.05
money = total_tax - expenses

print(f'{money:.2f}')