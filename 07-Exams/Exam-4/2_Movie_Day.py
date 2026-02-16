filming_time_available = int(input())
scenes_count = int(input())
scene_duration = int(input())

preparation_time = filming_time_available * 0.15
scenes_time = scenes_count * scene_duration
time_needed = scenes_time + preparation_time

if filming_time_available >= time_needed:
    remaining_time = round(filming_time_available - time_needed)
    print(f'You managed to finish the movie on time! You have {remaining_time}'
          f' minutes left!')

elif filming_time_available < time_needed:
    needed_time = round(time_needed - filming_time_available)
    print(f'Time is up! To complete the movie you need {needed_time} minutes.')