steps_goal = 10000
steps_walked = 0

command = input()

while command != 'Going home':
    steps = int(command)
    steps_walked += steps

    if steps_walked >= steps_goal:
        break

    command = input()

if command == 'Going home':
    steps_home = int(input())
    steps_walked += steps_home

if steps_walked >= steps_goal:
    print(f'Goal reached! Good job!')
    print(f'{steps_walked - steps_goal} steps over the goal.')

else:
    print(f'{steps_goal - steps_walked} more steps to reach goal.')