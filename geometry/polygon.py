def calculate_polygon_area(sides, lengths):

    if sides < 3 or len(lengths) != sides:
        raise ValueError("Неправильное количество сторон или длин сторон")

    area = 0.0
    for i in range(sides):
        j = (i + 1) % sides
        area += lengths[i] * lengths[j]

    area = abs(area) / 2.0
    return area
