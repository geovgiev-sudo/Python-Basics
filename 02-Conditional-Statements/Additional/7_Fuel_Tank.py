fuel_type = str(input())
litres = float(input())

if fuel_type == 'Diesel':
    if litres >= 25:
        print(f'You have enough diesel.')
    elif litres < 25:
        print(f'Fill your tank with diesel!')

# ВАЖНО
# Използваме elif тук, за да станат взаимоизкрючващи се проверките,
# иначе не става, просто влиза в друг if и накрая гърми.

elif fuel_type == 'Gasoline':
    if litres >= 25:
        print(f'You have enough gasoline.')
    elif litres < 25:
        print(f'Fill your tank with gasoline!')

# ВАЖНО
# Използваме elif тук, за да станат взаимоизкрючващи се проверките,
# иначе не става, просто влиза в друг if и накрая гърми.

elif fuel_type == 'Gas':
    if litres >= 25:
        print(f'You have enough gas.')
    elif litres < 25:
        print(f'Fill your tank with gas!')

else:
    print('Invalid fuel!')

# АТЕРНАТИВНО РЕШЕНИЕ

# fuel_type = input()
# litres = float(input())
#
# if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
#     if litres >= 25:
#         print(f"You have enough {fuel_type}.")
#     else:
#         print(f"Fill your tank with {fuel_type}!")
# else:
#     print("Invalid fuel!")


# РЕШЕНИЕ СЪС СПИСЪЦИ

# fuel_type = input()
# litres = float(input())
#
# valid_fuels = ["Diesel", "Gasoline", "Gas"]
#
# if fuel_type not in valid_fuels:
#     print("Invalid fuel!")
# else:
#     if litres >= 25:
#         print(f"You have enough {fuel_type}.")
#     else:
#         print(f"Fill your tank with {fuel_type}!")