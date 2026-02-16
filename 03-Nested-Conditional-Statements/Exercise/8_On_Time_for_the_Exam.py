exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_total_minutes = exam_hour * 60 + exam_minute
arrival_total_minutes = arrival_hour * 60 + arrival_minute


difference = exam_total_minutes - arrival_total_minutes

if difference < 0:
    print('Late')
elif (difference >= 0) and (difference <= 30):
    print('On time')
elif difference > 30:
    print('Early')


if 0 < difference < 60:
    print(f'{difference} minutes before the start')
elif difference >= 60:
    hour = difference // 60
    minute = difference % 60
    print(f'{hour}:{minute:02d} hours before the start')

elif -60 < difference < 0:
    print(f'{abs(difference)} minutes after the start')

elif difference <= -60:
    difference = abs(difference)
    hour = difference // 60
    minute = difference % 60
    print(f'{hour}:{minute:02d} hours after the start')