from math import floor

record = float(input())
distance = float(input())
metre_per_second = float(input())

time = distance * metre_per_second
delay = floor(distance / 50) * 30
time_total = time + delay

if time_total < record:
    print(f'Yes! The new record is {time_total:.2f} seconds.')
elif time_total >= record:
    time_needed = time_total - record
    print(f'No! He was {time_needed:.2f} seconds slower.')