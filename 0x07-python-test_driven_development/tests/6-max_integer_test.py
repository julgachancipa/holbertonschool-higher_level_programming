#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_right_cases(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer(["abc", "ab"]), "abc")
        self.assertEqual(max_integer(["za", "zz", "Zz"]), "zz")
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([(1, 2), (1, 3)]), (1, 3))
        self.assertEqual(max_integer([[1, 3], [1, 2]]), [1, 3])
        self.assertEqual(max_integer([1.2, -1.5, 1]), 1.2)
        self.assertEqual(max_integer(['b', 'a', 'Z']), 'b')
        self.assertEqual(max_integer([2, True, False]), 2)

    def test_wrong_cases(self):
        self.assertRaises(TypeError, max_integer, [1, 3, "oli", 2])
        self.assertRaises(TypeError, max_integer, [1.4, (2, 1), 2.7])
        self.assertRaises(TypeError, max_integer, [1.4, [2, 1], 2.7])
        self.assertRaises(TypeError, max_integer, [{"b": 1}, {"z": 1}])
        self.assertRaises(TypeError, max_integer, [None, 1])
        self.assertRaises(TypeError, max_integer, [None, None])
