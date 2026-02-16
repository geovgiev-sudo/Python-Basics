loads = int(input())
microbus_ton = 200
kamion_ton = 175
train_ton = 120
total_tons = 0
p1 = 0
p2 = 0
p3 = 0
t1 = 0
t2 = 0
t3 = 0

for i in range(1, loads + 1):
    tons_per_load = int(input())
    total_tons += tons_per_load
    if 3 >= tons_per_load:
        p1 += microbus_ton * tons_per_load
        t1 += tons_per_load
    elif 4 <= tons_per_load <= 11:
        p2 += kamion_ton * tons_per_load
        t2 += tons_per_load
    elif 12 <= tons_per_load:
        p3 += train_ton * tons_per_load
        t3 += tons_per_load

total_price = p1 + p2 + p3
average_price = total_price / total_tons
p1_percent = f'{t1 / total_tons * 100:.2f}%'
p2_percent = f'{t2 / total_tons * 100:.2f}%'
p3_percent = f'{t3 / total_tons * 100:.2f}%'

print(f'{average_price:.2f}')
print(f'{p1_percent}')
print(f'{p2_percent}')
print(f'{p3_percent}')