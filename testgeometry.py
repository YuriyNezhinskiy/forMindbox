import unittest
from geometry.circle import calculate_circle_area
from geometry.triangle import calculate_triangle_area


class TestMyGeometryFunctions(unittest.TestCase):

    def test_calculate_circle_area(self):
        # Проверка правильности вычисления площади круга
        self.assertAlmostEqual(calculate_circle_area(0), 0, places=2)
        self.assertAlmostEqual(calculate_circle_area(1), 3.14159, places=2)
        self.assertAlmostEqual(calculate_circle_area(5), 78.53982, places=2)

    def test_calculate_triangle_area(self):
        # Проверка правильности вычисления площади треугольника
        self.assertAlmostEqual(calculate_triangle_area(3, 4, 5), 6.0, places=2)
        self.assertAlmostEqual(calculate_triangle_area(6, 8, 10), 24.0, places=2)
        self.assertAlmostEqual(calculate_triangle_area(7, 7, 7), 21.2176, places=2)

    def test_negative_radius(self):
        # Проверка на отрицательный радиус
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)

    def test_negative_sides(self):
        # Проверка на отрицательные стороны треугольника
        with self.assertRaises(ValueError):
            calculate_triangle_area(-3, 4, 5)

    def test_invalid_triangle(self):
        # Проверка на невозможность построения треугольника
        with self.assertRaises(ValueError):
            calculate_triangle_area(1, 1, 3)


if __name__ == '__main__':
    unittest.main()
