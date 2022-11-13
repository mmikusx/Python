# wielomiany sa reprezentowane w sposob [a0, a1, a2] = a0*x*x + a1*x + a2

import unittest
from polys import *

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [-3, 0, 1, 2]      # W(x) = -3x^3 + x + 2
        self.p2 = [1, 0, -3, 11]   # W(x) = x^3 - 3x + 11
        self.p3 = [7, 0, 3, -1, 3] # W(x) = 7x^4 + 3x^2 - x + 3
        self.p4 = [1, 1] # W(x) = x + 1

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [-2, 0, -2, 13])
        self.assertEqual(add_poly(self.p1, self.p3), [7, -3, 3, 0, 5])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [-4, 0, 4, -9])
        self.assertEqual(sub_poly(self.p2, self.p3), [-7, 1, -3, -2, 8])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [-3, 0, 10, -31, -3, 5, 22])
        self.assertEqual(mul_poly(self.p2, self.p4), [1, 1, -3, 8, 11])

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 0, 0]), True)
        self.assertEqual(is_zero([1, 0, 0, 0]), False)

    def test_eq_poly(self):
        self.assertEqual(eq_poly(self.p4, [0, 1, 1]), True)
        self.assertEqual(eq_poly(self.p1, self.p2), False)

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p2, 2), 13)
        self.assertEqual(eval_poly(self.p3, 1), 12)

    def test_combine_poly(self):
        self.assertEqual(combine_poly([3, 2, -1], [2, -1]), [12, -8, 0])
        self.assertEqual(combine_poly(self.p2, self.p4), [1, 3, 0, 9])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p4, 2), [1, 2, 1])
        self.assertEqual(pow_poly(self.p4, 3), [1, 3, 3, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p3), [28, 0, 6, -1])
        self.assertEqual(diff_poly(self.p2), [3, 0, -3])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy