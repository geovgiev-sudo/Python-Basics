n = int(input())
l = int(input())

for s1 in range(1, n):
    for s2 in range(1, n):
        for s3 in range(97, l + 97):
            s3 = chr(s3)
            for s4 in range(97, l + 97):
                s4 = chr(s4)
                for s5 in range(max(s1, s2) + 1, n + 1):
                    print(f'{s1}{s2}{s3}{s4}{s5}', end=' ')