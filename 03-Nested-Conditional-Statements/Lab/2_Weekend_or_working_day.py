day = input()
result = ''

# Същата е като предишната задача

if (day == 'Monday'
        or day == 'Tuesday'
        or day == 'Wednesday'
        or day == 'Thursday'
        or day == 'Friday'):
    print('Working day')
elif (day == 'Saturday'
        or day == 'Sunday'):
    print('Weekend')
else:
    result = 'Error'
print(result)

