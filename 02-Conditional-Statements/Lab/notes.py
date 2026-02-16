day_of_the_week = "Friday"
income = 0 #глобална променлива - тук е дефинирана, но тя може да присвои друга стойност в if
if day_of_the_week == "Monday":
    income = 350 #тази променлива живее само тук. Тя е инициирана само в този блок код.
else:
    print("No income")

print (income)


# видове променливи local, enclosing, global, built-in
# много е важно да се декларират правилно променливите


# a = 7
#
# if a > 4:
#     print('Bigger than 4')
# elif a > 5:
#     print('Bigger than 5')
# else:
#     print('Equal to 7')
#


# from math import ceil, floor
# a = 5.9345839736
#
# print(f"{a:.2f}")
# print(round(a, 6))
#
#
# # print (abs(b))
#
# # print(round(a, 2))
# # print(ceil(a))
