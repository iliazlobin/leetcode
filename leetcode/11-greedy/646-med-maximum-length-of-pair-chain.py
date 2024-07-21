import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findLongestChain_example1(self):
        pairs = [[1, 2], [2, 3], [3, 4]]
        expected = 2
        result = self.solution.findLongestChain(pairs)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_findLongestChain_example2(self):
        pairs = [[1, 2], [7, 8], [4, 5]]
        expected = 3
        result = self.solution.findLongestChain(pairs)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_findLongestChain_custom(self):
        pairs = [[-6, 9], [1, 6], [8, 10], [-1, 4], [-6, -2], [-9, 8], [-5, 3], [0, 3]]
        expected = 3
        result = self.solution.findLongestChain(pairs)
        self.assertEqual(expected, result, f"Failed on custom test with {result} != {expected}")

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda p: p[1])

        res = 1
        longest = pairs[0]
        for p in pairs:
            if p[0] > longest[1]:
                longest[1] = p[1]
                res += 1

        return res


if __name__ == "__main__":
    unittest.main()
