def calculate_polygon_properties(length, width):
    if length == width:
       
        area = length ** 2
        return area
    else:
       
        perimeter = 2 * (length + width)
        return perimeter


print(calculate_polygon_properties(6, 10)) 
print(calculate_polygon_properties(3, 3))   