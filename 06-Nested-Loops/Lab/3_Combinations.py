n = int(input())
counter = 0
iteration = 0

for n1 in range(n + 1):
    for n2 in range(n + 1):
        for n3 in range(n + 1):
            iteration += 1
            total = (n1 + n2 + n3)
            if total == n:
                counter += 1
                break
print(counter)