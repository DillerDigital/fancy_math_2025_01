import unittest

from fancymath.fancy_math import fact, is_even


class TestFancyMath(unittest.TestCase):
    def test_fact(self):
        "test the factorial function"
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(4), 24)
        self.assertEqual(fact(0), 1)

    def test_fact_negative(self):
        "test that factorial behaves properly with negative numbers"
        with self.assertRaises(ValueError):
            fact(-1)

    # def test_membership(self):
    #     "Regression test for Issue #567"
    #     my_set = {1, 2, 3}
    #     self.assertIn(4, my_set)

    # def test_list_equal(self):
    #     my_list = [1, 2, 3]
    #     self.assertListEqual([1, 3], my_list)

    def test_is_even(self):
        "test the is_even function"
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(1.1))

if __name__ == '__main__':
    unittest.main()