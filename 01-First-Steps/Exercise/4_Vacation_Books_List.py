pages_in_book = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

total_per_book = pages_in_book / pages_per_hour

hours_per_day = int(total_per_book / days_to_read)

# or
# hours_per_day = total_per_book // days_to_read
# or
# print(int)(hours_per_day)

print(hours_per_day)
