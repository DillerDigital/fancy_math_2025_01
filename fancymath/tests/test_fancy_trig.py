import math
import random
import unittest

from fancymath.fancy_trig import gauss_sum


class TestGuassianSum(unittest.TestCase):
    def test_gauss_sum_5(self):
        n = 5
        expected = 5 + 4 + 3 + 2 + 1

        result = gauss_sum(n)
        self.assertEqual(expected, result)