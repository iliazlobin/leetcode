import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxProduct(self):
        self.assertEqual(self.solution.maxProduct([2, 3, -2, 4]), 6, "Example 1 failed")
        self.assertEqual(self.solution.maxProduct([-2, 0, -1]), 0, "Example 2 failed")
        self.assertEqual(self.solution.maxProduct([-2]), -2, "Example 2 failed")
        self.assertEqual(self.solution.maxProduct([0, 2]), 2, "Example 2 failed")
        self.assertEqual(
            self.solution.maxProduct([2, -5, -2, -4, 3]),
            24,
            "Failed for input: [2,-5,-2,-4,3]",
        )


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)

        return res


if __name__ == "__main__":
    unittest.main()
