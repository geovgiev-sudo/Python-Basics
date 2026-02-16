budget = float(input())
gpus = int(input())
cpus = int(input())
rams = int(input())

gpu_price = 250
gpu_sum = gpus * gpu_price

cpu_price = 0.35 * gpu_sum
cpu_sum = cpus * cpu_price

ram_price = 0.10 * gpu_sum
ram_sum = rams * ram_price

total_sum = gpu_sum + cpu_sum + ram_sum

if gpus > cpus:
    total_sum *= 0.85

difference = abs(total_sum - budget)

if total_sum <= budget:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')