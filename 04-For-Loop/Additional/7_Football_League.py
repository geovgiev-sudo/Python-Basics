capacity = int(input())
fans = int(input())
sector = ''
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for i in range(fans):
    sector = input()
    if sector == 'A':
        fans_a += 1
    elif sector == 'B':
        fans_b += 1
    elif sector == 'V':
        fans_v += 1
    elif sector == 'G':
        fans_g += 1

fans_total = fans_a + fans_b + fans_v + fans_g

fans_a_percent = f'{fans_a / fans * 100:.2f}%'
fans_b_percent = f'{fans_b / fans * 100:.2f}%'
fans_v_percent = f'{fans_v / fans * 100:.2f}%'
fans_g_percent = f'{fans_g / fans * 100:.2f}%'
fans_total_percent = f'{fans_total / capacity * 100:.2f}%'

print(f'{fans_a_percent}')
print(f'{fans_b_percent}')
print(f'{fans_v_percent}')
print(f'{fans_g_percent}')
print(f'{fans_total_percent}')