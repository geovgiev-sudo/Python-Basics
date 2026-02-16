from math import ceil

show = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
rest_time = break_length / 4

time_left = break_length - lunch_time - rest_time

difference = abs(episode_length - time_left)

if time_left >= episode_length:
    print(f'You have enough time to watch {show} and left with {ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {show}, you need {ceil(difference)} more minutes.")

# if time_left >= episode_length:
#     free_time = time_left - episode_length
#     print(f'You have enough time to watch {show} and left with {ceil(free_time)} minutes free time.')
# else:
#     need_time = episode_length - time_left
#     print(f"You don't have enough time to watch {show}, you need {ceil(need_time)} more minutes.")