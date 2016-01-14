"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type, get_rectangle_type, get_shape_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_all_int(self):
        result = get_triangle_type(0, 1, 2)
        self.assertEqual(result, 'invalid')

class TestGetRectangleType(TestCase):

    def test_get_rectangle_square_all_int(self):
        result = get_rectangle_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_all_int(self):
        result = get_rectangle_type(1, 1, 2, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_invalid_all_int(self):
        result = get_rectangle_type(0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

class TestGetShapeType(TestCase):

    def test_get_shape_square_all_int(self):
        result = get_shape_type(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_shape_rectangle_all_int(self):
        result = get_shape_type(1, 1, 2, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_shape_rhombus_all_int(self):
        result = get_shape_type(1, 1, 1, 1, 45, 45, 135, 135)
        self.assertEqual(result, 'rhombus')

    def test_get_shape_disconnected_all_int(self):
        result = get_shape_type(1, 1, 1, 1, 50, 50, 50, 50)
        self.assertEqual(result, 'disconnected')