series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_duration = float(input())

reklami_duration = episode_duration * 0.20
episode_duration_reklami = episode_duration + reklami_duration
extra_time = seasons_count * 10
time_needed = episode_duration_reklami * episodes_count * seasons_count + extra_time

print(f'Total time needed to watch the {series_name} series is {round(time_needed)} minutes.')