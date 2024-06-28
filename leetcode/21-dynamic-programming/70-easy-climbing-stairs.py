import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climbStairs(self):
        self.assertEqual(self.solution.climbStairs(2), 2, "Example 1 failed")
        self.assertEqual(self.solution.climbStairs(3), 3, "Example 2 failed")
        self.assertEqual(self.solution.climbStairs(4), 5, "Example 3 failed")


class RSolution:
    def climbStairs(self, n: int) -> int:
        def dfs(pos):
            if n - pos == 1:
                return 1
            if n - pos == 2:
                return 2
            # n = 5, pos = 2, diff = 3
            return dfs(pos + 1) + dfs(pos + 2)

        return dfs(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp

        return n2


if __name__ == "__main__":
    unittest.main()
