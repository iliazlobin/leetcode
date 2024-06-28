import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLIS(self):
        self.assertEqual(
            self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]),
            4,
            "Example 1 failed",
        )

        self.assertEqual(
            self.solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4, "Example 2 failed"
        )

        self.assertEqual(
            self.solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1, "Example 3 failed"
        )


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])

        return max(res)


if __name__ == "__main__":
    unittest.main()
