from geometry.circle import calculate_circle_area
from geometry.triangle import calculate_triangle_area
from geometry.polygon import calculate_polygon_area


def calculate_area(*args):

    if len(args) == 1:
        return calculate_circle_area(args[0])
    elif len(args) == 3:
        return calculate_triangle_area(*args)
    elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], list):
        return calculate_polygon_area(args[0], args[1])
    else:
        raise ValueError("Неподдерживаемый набор аргументов для вычисления площади")