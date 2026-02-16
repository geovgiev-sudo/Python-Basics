rent = int(input())

statuet_price = rent * 0.70
catering_price = statuet_price * 0.85
sound_price = catering_price / 2

total_sum = (rent + statuet_price
             + catering_price
             + sound_price)

print(f'{total_sum:.2f}')