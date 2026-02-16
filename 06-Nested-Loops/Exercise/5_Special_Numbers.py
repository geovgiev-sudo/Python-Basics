# n = int(input())
#
# for d1 in range(1, 10):
#     for d2 in range(1, 10):
#         for d3 in range(1, 10):
#             for d4 in range(1, 10):
#                 check1 = (n % d1 == 0)
#                 check2 = (n % d2 == 0)
#                 check3 = (n % d3 == 0)
#                 check4 = (n % d4 == 0)
#
#                 if check1 and check2 and check3 and check4:
#                     print(f"{d1}{d2}{d3}{d4}", end=" ")




# n = int(input())
#
# for number in range(1111, 9999 + 1):
#     number_str = str(number)
#     is_special = True
#
#     for index, char_digit in enumerate(number_str): # enumerate прави tuple, който съдържа позиция и цифрата като стринг
#         # трябват затова две променливи в цикъла
#         int_digit = int(char_digit) # превръщаме стринг в интегер
#         if int_digit == 0:
#             is_special = False
#             break
#
#         if n % int_digit != 0:
#             is_special = False
#             break
#
#     if is_special:
#         print(number, end= ' ')


n = int(input())

for number in range(1111, 9999 + 1):
    number_str = str(number)
    is_special = True

    for char_digit in number_str:
        int_digit = int(char_digit) # превръщаме стринг в интегер

        if int_digit == 0 or n % int_digit != 0:
            is_special = False
            break

    if is_special:
        print(number, end= ' ')