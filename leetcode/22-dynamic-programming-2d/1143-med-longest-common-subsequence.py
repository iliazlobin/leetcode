import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestCommonSubsequence(self):
        self.assertEqual(
            self.solution.longestCommonSubsequence("abcde", "ace"),
            3,
            "Example 1 failed",
        )

        self.assertEqual(
            self.solution.longestCommonSubsequence("abc", "abc"), 3, "Example 2 failed"
        )

        self.assertEqual(
            self.solution.longestCommonSubsequence("abc", "def"), 0, "Example 3 failed"
        )


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for r in range(len(grid) - 2, -1, -1):
            for c in range(len(grid[0]) - 2, -1, -1):
                if text2[c] == text1[r]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                else:
                    grid[r][c] = max(grid[r][c + 1], grid[r + 1][c])

        return grid[0][0]

if __name__ == "__main__":
    unittest.main()
