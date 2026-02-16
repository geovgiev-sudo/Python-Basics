time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60 # тоест като го разделим на 60, кое е най-близкото цяло число
seconds = total_time % 60 # тоест като го разделим на 60, колко ще остане?

print(f'{minutes}:{seconds:02d}') # Слагаме водеща нула

# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')