nailon_per_metre = 1.50
boya_per_litre = 14.50
razreditel_per_litre = 5.00
torbi4ki = 0.40

metres_nailon = int(input())
litres_boya = int(input())
litres_razreditel = int(input())
hours_work = int(input())

total_nailon = metres_nailon + 2
total_boya = litres_boya * 1.10

total_sum_nailon = total_nailon * nailon_per_metre
total_sum_boya = total_boya * boya_per_litre
total_sum_razreditel = litres_razreditel * razreditel_per_litre

total_sum_materiali = total_sum_nailon + total_sum_boya + total_sum_razreditel + torbi4ki

total_sum_maistori = (total_sum_materiali * 0.30) * hours_work

total_sum = total_sum_materiali + total_sum_maistori

print(f"{total_sum:.2f}")