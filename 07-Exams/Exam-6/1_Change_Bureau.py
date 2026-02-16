bitcoins = int(input())
china_yoan = float(input())
comission = float(input())

bitcoin = bitcoins * 1168
dollar = 1.76
evro = 1.95
china_dollars = 0.15 * china_yoan
china_leva = dollar * china_dollars

evra = (bitcoin + china_leva) / evro
commission = comission / 100 * evra
result = evra - commission
print(f'{result:.2f}')