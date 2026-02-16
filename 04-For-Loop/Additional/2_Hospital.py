days = int(input())
doctors = 7
patients = 0
treated_patients = 0
untreated_patients = 0

for day in range(1, days + 1):
    daily_patients = int(input())
    if day % 3 == 0:
        if untreated_patients > treated_patients:
         doctors += 1
    if daily_patients <= doctors:
        treated_patients += daily_patients
    elif daily_patients > doctors:
        untreated_patients += daily_patients - doctors
        treated_patients += doctors

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')