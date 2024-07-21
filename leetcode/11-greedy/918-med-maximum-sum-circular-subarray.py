import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxSubarraySumCircular(self):
        # Example 1
        nums = [1, -2, 3, -2]
        self.assertEqual(
            self.solution.maxSubarraySumCircular(nums), 3, "Failed for Example 1"
        )

        # Example 2
        nums = [5, -3, 5]
        self.assertEqual(
            self.solution.maxSubarraySumCircular(nums), 10, "Failed for Example 2"
        )

        # Example 3
        nums = [-3, -2, -3]
        self.assertEqual(
            self.solution.maxSubarraySumCircular(nums), -2, "Failed for Example 3"
        )

        nums = [-2, 4, -5, 4, -5, 9, 4]
        self.assertEqual(
            self.solution.maxSubarraySumCircular(nums),
            15,
            "Failed with shifted positive sum",
        )


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = localMax = float("-inf")
        globalMin = localMin = float("inf")
        total = 0

        for n in nums:
            total += n
            localMax = max(n, n + localMax)
            globalMax = max(globalMax, localMax)
            localMin = min(n, n + localMin)
            globalMin = min(globalMin, localMin)

        return max(total - globalMin, globalMax) if globalMax > 0 else globalMax


if __name__ == "__main__":
    unittest.main()
