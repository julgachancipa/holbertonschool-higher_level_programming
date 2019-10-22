#!/usr/bin/python3
"""
Unittest for base
"""
import unittest
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    def test_right_width_cases(self):
        self.assertEqual(Rectangle(1, 2).width, 1)
        self.assertEqual(Rectangle(3, 2, 3).width, 3)
        self.assertEqual(Rectangle(5, 2, 3, 4).width, 5)
        self.assertEqual(Rectangle(7, 2, 3, 4, 5).width, 7)
        self.assertEqual(Rectangle(9, 2, id=0).width, 9)
        self.assertEqual(Rectangle(11, 2, 3, id=-54).width, 11)
        self.assertEqual(Rectangle(13, 2, 3, 4, id=True).width, 13)
        self.assertEqual(Rectangle(15, 2, 3, 4, id='oli').width, 15)
        self.assertEqual(Rectangle(17, 2, 3, 4, id=(1, 2)).width, 17)
        self.assertEqual(Rectangle(19, 2, 3, 4, id=[1, 2]).width, 19)
        self.assertEqual(Rectangle(21, 2, 3, 4, id={'1': 2}).width, 21)

    def test_wrong_width_cases(self):
        self.assertRaises(TypeError, Rectangle, 'st', 1)
        self.assertRaises(TypeError, Rectangle, [1, 2], 3)
        self.assertRaises(TypeError, Rectangle, (1, 2), 6)
        self.assertRaises(TypeError, Rectangle, {'1': 2}, 5)
        self.assertRaises(TypeError, Rectangle, None, 3)
        self.assertRaises(TypeError, Rectangle, True, 3)
        self.assertRaises(TypeError, Rectangle, 2.56, 3)
        self.assertRaises(ValueError, Rectangle, 0, 3)
        self.assertRaises(ValueError, Rectangle, -5, 3)

    def test_right_height_cases(self):
        self.assertEqual(Rectangle(1, 2).height, 2)
        self.assertEqual(Rectangle(3, 2, 3).height, 2)
        self.assertEqual(Rectangle(5, 2, 3, 4).height, 2)
        self.assertEqual(Rectangle(7, 2, 3, 4, 5).height, 2)
        self.assertEqual(Rectangle(9, 2, id=0).height, 2)
        self.assertEqual(Rectangle(11, 2, 3, id=-54).height, 2)
        self.assertEqual(Rectangle(13, 2, 3, 4, id=True).height, 2)
        self.assertEqual(Rectangle(15, 2, 3, 4, id='oli').height, 2)
        self.assertEqual(Rectangle(17, 2, 3, 4, id=(1, 2)).height, 2)
        self.assertEqual(Rectangle(19, 2, 3, 4, id=[1, 2]).height, 2)
        self.assertEqual(Rectangle(21, 2, 3, 4, id={'1': 2}).height, 2)

    def test_wrong_height_cases(self):
        self.assertRaises(TypeError, Rectangle, 1, 'st')
        self.assertRaises(TypeError, Rectangle, 1, [1, 2])
        self.assertRaises(TypeError, Rectangle, 1, (1, 2))
        self.assertRaises(TypeError, Rectangle, 1, {'1': 2})
        self.assertRaises(TypeError, Rectangle, 1, None)
        self.assertRaises(TypeError, Rectangle, 2, True, 3)
        self.assertRaises(TypeError, Rectangle, 3, 2.56, 3)
        self.assertRaises(ValueError, Rectangle, 3, 0, 3)
        self.assertRaises(ValueError, Rectangle, 1, -5, 3)

    def test_right_x_cases(self):
        self.assertEqual(Rectangle(1, 2, 3).x, 3)
        self.assertEqual(Rectangle(1, 2).x, 0)
        self.assertEqual(Rectangle(1, 2, 0).x, 0)

    def test_wrong_x_cases(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 'st')
        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 1, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 1, 2, {'1': 2})
        self.assertRaises(TypeError, Rectangle, 1, 2, None)
        self.assertRaises(TypeError, Rectangle, 2, 2, True, 3)
        self.assertRaises(TypeError, Rectangle, 3, 2, 2.56, 3)
        self.assertRaises(ValueError, Rectangle, 1, 2, -5, 3)

    def test_right_y_cases(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)
        self.assertEqual(Rectangle(1, 2).y, 0)
        self.assertEqual(Rectangle(1, 2, 0, 0).y, 0)

    def test_wrong_y_cases(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 'st')
        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 1, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 1, 2, {'1': 2})
        self.assertRaises(TypeError, Rectangle, 1, 2, None)
        self.assertRaises(TypeError, Rectangle, 2, 2, True, 3)
        self.assertRaises(TypeError, Rectangle, 3, 2, 2.56, 3)
        self.assertRaises(ValueError, Rectangle, 1, 2, -5, 3)

    def test_right_id_cases(self):
        self.assertEqual(Rectangle(1, 2).id, 64)
        self.assertEqual(Rectangle(1, 2, 3).id, 65)
        self.assertEqual(Rectangle(1, 2, 3, 4).id, 66)
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)
        self.assertEqual(Rectangle(1, 2, id=0).id, 0)
        self.assertEqual(Rectangle(1, 2, 3, id=-54).id, -54)
        self.assertEqual(Rectangle(1, 2, 3, 4, id=True).id, 1)
        self.assertEqual(Rectangle(1, 2, 3, 4, id='oli').id, 'oli')
        self.assertEqual(Rectangle(1, 2, 3, 4, id=(1, 2)).id, (1, 2))
        self.assertEqual(Rectangle(1, 2, 3, 4, id=[1, 2]).id, [1, 2])
        self.assertEqual(Rectangle(1, 2, 3, 4, id={'1': 2}).id, {'1': 2})

    def test_right_area_cases(self):
        self.assertEqual(Rectangle(1, 2).area(), 2)
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_right_update_args_cases(self):
        R = Rectangle(1, 2)
        R.update(9)
        self.assertEqual(R.id, 9)
        R.update(9, 8, 9)
        self.assertEqual(R.width, 8)
        R.update(92, 81, 91)
        self.assertEqual(R.height, 91)
        R.update(92, 81, 91, 100)
        self.assertEqual(R.x, 100)
        R.update(92, 8, 1, 9, 10)
        self.assertEqual(R.x, 9)
        self.assertEqual(R.y, 10)

    def test_right_update_kwargs_cases(self):
        R = Rectangle(1, 2)
        R.update(id=9)
        self.assertEqual(R.id, 9)
        R.update(x=9, width=8, y=9)
        self.assertEqual(R.width, 8)
        R.update(height=92, y=81, x=91)
        self.assertEqual(R.height, 92)
        R.update(id=92, width=81, height=91, x=100)
        self.assertEqual(R.x, 100)
        R.update(id=92, width=8, height=1, x=9, y=10)
        self.assertEqual(R.x, 9)
        self.assertEqual(R.y, 10)

    def test_wrong_init_cases(self):
        self.assertRaises(TypeError, Rectangle, n=0)
        self.assertRaises(TypeError, Rectangle, None)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)
