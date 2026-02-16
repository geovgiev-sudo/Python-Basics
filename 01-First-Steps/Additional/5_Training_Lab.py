length = float(input())
width = float(input())
columns = (width * 100 - 100) // 70
rows = length * 100 // 120
result = columns * rows - 3
print(result)