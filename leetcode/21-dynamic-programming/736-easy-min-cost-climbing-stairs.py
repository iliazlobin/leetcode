import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minCostClimbingStairs(self):
        self.assertEqual(
            self.solution.minCostClimbingStairs([10, 15, 20]), 15, "Example 1 failed"
        )
        self.assertEqual(
            self.solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
            6,
            "Example 2 failed",
        )


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


if __name__ == "__main__":
    unittest.main()
