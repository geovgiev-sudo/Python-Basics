type = input()

#shape_area = 0.0

if type == "square":
    side = float(input())
    face = side * side
    print(f"{face:.3f}")

elif type == "rectangle":
    a = float(input())
    b = float(input())
    c = a * b
    print(f"{c:.3f}")

elif type == "circle":
    from math import pi
    r = float(input())
    a = pi * (r * r)
    print(f"{a:.3f}")

elif type == "triangle":
    a = float(input())
    h = float(input())
    c = a * h / 2
    print(f"{c:.3f}")


#print(f"{shape_area:.3f})


