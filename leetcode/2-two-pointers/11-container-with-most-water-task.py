import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxArea_examples(self):
        heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected1 = 49
        self.assertEqual(
            self.solution.maxArea(heights1), expected1, f"Failed for input: {heights1}"
        )

        heights2 = [1, 1]
        expected2 = 1
        self.assertEqual(
            self.solution.maxArea(heights2), expected2, f"Failed for input: {heights2}"
        )


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return None


if __name__ == "__main__":
    unittest.main()
