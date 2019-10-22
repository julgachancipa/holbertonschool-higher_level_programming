#!/usr/bin/python3
"""
Unittest for base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_right_id_cases(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(-1).id, -1)
        self.assertEqual(Base(48).id, 48)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(2).id, 2)
        self.assertEqual(Base(None).id, 3)
        self.assertEqual(Base(True).id, 1)
        self.assertEqual(Base(False).id, 0)
        self.assertEqual(Base('1').id, '1')
        self.assertEqual(Base([1, 2]).id, [1, 2])
        self.assertEqual(Base({'1': 2}).id, {'1': 2})
        self.assertEqual(Base(('1', 2)).id, ('1', 2))
        self.assertEqual(Base(id=5741).id, 5741)
        self.assertEqual(Base([]).id, [])
        self.assertEqual(Base(()).id, ())
        self.assertEqual(Base(3.1416).id, 3.1416)

    def test_wrong_init_cases(self):
        self.assertRaises(TypeError, Base, n=0)
        self.assertRaises(TypeError, Base, 1, 2)
        self.assertRaises(TypeError, Base, '1', 2)
        self.assertRaises(TypeError, Base, '1', '2', 3, {'1': 2})
        self.assertRaises(TypeError, Base, (1, 2), 1, [1, 3], '1')
        self.assertRaises(TypeError, Base, id=0, n=0)
        self.assertRaises(TypeError, Base, None, None)
        self.assertRaises(TypeError, Base, True, False)
