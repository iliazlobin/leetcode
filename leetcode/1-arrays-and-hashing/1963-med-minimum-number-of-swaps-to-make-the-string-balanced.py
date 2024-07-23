import math
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minSwaps_example1(self):
        s = "][]["
        expected = 1
        result = self.solution.minSwaps(s)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_minSwaps_example2(self):
        s = "]]][[["
        expected = 2
        result = self.solution.minSwaps(s)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_minSwaps_example3(self):
        s = "[]"
        expected = 0
        result = self.solution.minSwaps(s)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        for c in s:
            if c == "[":
                imbalance += 1
            elif imbalance > 0:
                imbalance -= 1
        return (imbalance + 1) // 2


if __name__ == "__main__":
    unittest.main()
