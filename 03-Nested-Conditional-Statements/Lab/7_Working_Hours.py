hour = int(input())
day = input()

if (10 <= hour <= 18) and (day == 'Monday'
                           or 'Tuesday'
                           or 'Wednesday'
                           or 'Thursday'
                           or 'Friday'
                           or 'Saturday'):
    print('open')
else:
    print('closed')
