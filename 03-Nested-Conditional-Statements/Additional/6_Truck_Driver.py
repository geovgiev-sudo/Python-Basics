season = input()
kms_per_month = float(input())
pay_per_km = 0

if 5000 >= kms_per_month:
    if season == 'Spring' or season == 'Autumn':
        pay_per_km = 0.75
    elif season == 'Summer':
        pay_per_km = 0.90
    elif season == 'Winter':
        pay_per_km = 1.05

elif 5000 < kms_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        pay_per_km = 0.95
    elif season == 'Summer':
        pay_per_km = 1.10
    elif season == 'Winter':
        pay_per_km = 1.25

elif 10000 < kms_per_month <= 20000:
        pay_per_km = 1.45

salary_per_month = kms_per_month * pay_per_km
salary = salary_per_month * 4
salary_after_tax = salary * 0.90
print(f'{salary_after_tax:.2f}')