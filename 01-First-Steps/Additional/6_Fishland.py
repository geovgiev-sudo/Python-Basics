skumria_price_per_kg = float(input())
zaza_price_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price_per_kg = skumria_price_per_kg + (skumria_price_per_kg * 0.60)
safrid_price_per_kg = zaza_price_per_kg + (zaza_price_per_kg * 0.80)
midi_price_per_kg = 7.50

total_price_palamud = palamud_price_per_kg * palamud_kg
total_price_safrid = safrid_price_per_kg * safrid_kg
total_price_midi = midi_price_per_kg * midi_kg

total = total_price_palamud + total_price_safrid + total_price_midi

print(f"{total:.2f}")