import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.minimumDifference([90], 1), 0)

    def test_example2(self):
        self.assertEqual(self.solution.minimumDifference([9, 4, 1, 7], 2), 2)


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float("inf")
        l = 0
        for r in range(len(nums)):
            if r - l + 1 == k:
                res = min(res, nums[r] - nums[l])
                l += 1
        return res


if __name__ == "__main__":
    unittest.main()
