import math


def calculate_triangle_area(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Длины сторон должны быть положительными числами")

    # Проверка на неравенство треугольника
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise ValueError("Невозможно построить треугольник с данными сторонами")

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area
