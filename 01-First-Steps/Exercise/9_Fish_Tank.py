length = int(input())
width = int(input())
height = int(input())
protzent = float(input())

volume_cm3 = length * width * height
volume_litres = volume_cm3 * 0.001 # or obem_akvarium / 1000
used_space = protzent / 100
usable_litres = volume_litres * (1 - used_space)

print(usable_litres)
