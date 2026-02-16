rest_days = int(input())

game_time_norm = 30000
minutes_to_play_work = 63
minutes_to_play_rest = 127

year = 365

play_time_when_working = (year - rest_days) * minutes_to_play_work
play_time_when_resting = rest_days * minutes_to_play_rest

total_playtime = play_time_when_resting + play_time_when_working
difference = abs(game_time_norm - total_playtime)
h = difference // 60
m = difference % 60

if total_playtime > game_time_norm:
    print(f'Tom will run away')
    print(f'{h} hours and {m} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{h} hours and {m} minutes less for play')