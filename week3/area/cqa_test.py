import unittest
import convex_quadrilateral_area as cqa

class TestConvexQuadrilateralArea(unittest.TestCase):

    def test_lines_intersection(self):
        self.assertEqual(cqa.lines_intersection(1, 2, -1, 2), (0, 2))
        self.assertEqual(cqa.lines_intersection(1, 2, 1, -2), None)
        self.assertEqual(cqa.lines_intersection(0, 0, 0, 0), None)

    def test_distance(self):
        self.assertEqual(cqa.distance(0, 0, 3, 4), 5.00)
        self.assertEqual(cqa.distance(-1, -1, 1, 1), 2.83)
        self.assertEqual(cqa.distance(0, 0, 0, 0), 0.00)

    def test_quadrangle_area(self):
        self.assertEqual(cqa.quadrangle_area(3, 4, 3, 4, 5, 5), 12.00)

    def test_four_lines_area(self):
        self.assertEqual(cqa.four_lines_area(1, 0, 1, 2, 1, 4, 1, 6), 0)
        self.assertEqual(cqa.four_lines_area(0, 0, 0, 0, 0, 0, 0, 0), 0)

    def test_lines_intersection_vertical(self):
        self.assertEqual(cqa.lines_intersection(float('inf'), 0, float('inf'), 2), None)

    def test_lines_intersection_parallel(self):
        self.assertEqual(cqa.lines_intersection(1, 0, 1, 2), None)

    def test_distance_negative(self):
        self.assertEqual(cqa.distance(0, 0, -3, -4), 5.00)

    def test_quadrangle_area_invalid(self):
        self.assertEqual(cqa.quadrangle_area(1, 1, 1, 3, 1, 1), None)

    def test_quadrangle_area_non_cyclic(self):
        self.assertEqual(cqa.quadrangle_area(3, 4, 3, 4, 5, 6), 14.59)

    def test_four_lines_area_parallel(self):
        self.assertEqual(cqa.four_lines_area(1, 0, 1, 2, -1, 0, -1, 2), 0)

    def test_four_lines_area_single_point(self):
        self.assertEqual(cqa.four_lines_area(1, 0, -1, 0, 1, 0, -1, 0), 0)
if __name__ == '__main__':
    unittest.main()