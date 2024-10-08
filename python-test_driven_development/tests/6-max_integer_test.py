#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_usual_cases(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
    def test_single_number(self):
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-10]), -10)
    
    def test_identical_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_number_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.1, 1.2, 1.0]), 1.2)
