x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 * 1.5
total_side_wall = (side_wall + side_wall) - (window + window)
back_wall = x * x
entrance = 1.2 * 2
front_wall = x * x
total_front_back_wall = front_wall + back_wall - entrance
total_house_area = total_side_wall + total_front_back_wall
total_litres_green_paint = total_house_area / 3.4

roof_rectangle_area = x * y
roof_triangle_area = x * h / 2
total_roof_rectangles = roof_rectangle_area + roof_rectangle_area
total_roof_triangles = roof_triangle_area + roof_triangle_area
total_roof_area = total_roof_rectangles + total_roof_triangles
total_litres_red_paint = total_roof_area / 4.3

print(f"{total_litres_green_paint:.2f}")
print(f"{total_litres_red_paint:.2f}")