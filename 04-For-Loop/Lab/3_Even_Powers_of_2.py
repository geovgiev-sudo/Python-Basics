# n = int(input())
# num = 1
# for i in range(0, n + 1, 2):
#   print(num)
#   num = num * 2 * 2

# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8

n = int(input())
for power in range(n + 1): # слагаме + 1, за да включим и числото n
    # print(power)
    if power % 2 == 0:
        result = 2 ** power # Повдигаме 2 на съответната степен
        print(result)
