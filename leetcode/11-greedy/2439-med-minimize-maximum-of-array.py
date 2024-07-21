import math
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimizeArrayValue_example1(self):
        self.assertEqual(
            self.solution.minimizeArrayValue([3, 7, 1, 6]), 5, "Example 1 failed."
        )

    def test_minimizeArrayValue_example2(self):
        self.assertEqual(
            self.solution.minimizeArrayValue([10, 1]), 10, "Example 2 failed."
        )


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # [3, 7, 1, 6]
        res = total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, math.ceil(total / (i + 1)))
        return res


if __name__ == "__main__":
    unittest.main()
