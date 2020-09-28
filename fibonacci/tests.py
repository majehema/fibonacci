
# Create your tests here.
import unittest

from fibonacci.fibonacci import calc_seq


class MyTestCase(unittest.TestCase):

    def test_nine(self):
        result = calc_seq(9)
        self.assertEqual(result, [[2, 2, 2, 3], [2, 2, 5], [3, 3, 3]])

    def test_eleven(self):
        result = calc_seq(11)
        self.assertEqual(result, [[2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [3, 8]])

    def test_seven(self):
        result = calc_seq(7)
        self.assertEqual(result, [[2, 2, 3], [2, 5]])

    def test_one(self):
        result = calc_seq(1)
        self.assertEqual(result, [])

    def test_zero(self):
        result = calc_seq(0)
        self.assertEqual(result, [])

    def test_negative(self):
        result = calc_seq(-5)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
