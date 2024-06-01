import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getSum(self):
        a = 1
        b = 1
        result = self.solution.getSum(a, b)
        self.assertEqual(result, 2)

        a = 4
        b = 7
        result = self.solution.getSum(a, b)
        self.assertEqual(result, 11)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp
        return a

if __name__ == "__main__":
    unittest.main()

