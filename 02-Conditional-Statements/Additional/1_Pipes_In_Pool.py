v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_fills = p1 * h
p2_fills = p2 * h
total_fills = p1_fills + p2_fills

if total_fills <= v:
    prozent1 = p1_fills / total_fills * 100 # Изчисляваме колко процента е
    prozent2 = p2_fills / total_fills * 100
    prozent_total = total_fills / v * 100
    print(f'The pool is {prozent_total:.2f}% full. Pipe 1: {prozent1:.2f}%. Pipe 2: {prozent2:.2f}%.')

elif total_fills > v:
    overflow = total_fills - v
    print(f'For {h} hours the pool overflows with {overflow} litres.')