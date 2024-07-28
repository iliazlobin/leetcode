import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxSubarrayLength_example1(self):
        nums = [1, 2, 3, 1, 2, 3, 1, 2]
        k = 2
        expected_output = 6
        self.assertEqual(self.solution.maxSubarrayLength(nums, k), expected_output)

    def test_maxSubarrayLength_example2(self):
        nums = [1, 2, 1, 2, 1, 2, 1, 2]
        k = 1
        expected_output = 2
        self.assertEqual(self.solution.maxSubarrayLength(nums, k), expected_output)

    def test_maxSubarrayLength_example3(self):
        nums = [5, 5, 5, 5, 5, 5, 5]
        k = 4
        expected_output = 4
        self.assertEqual(self.solution.maxSubarrayLength(nums, k), expected_output)


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        l = 0
        res = 0
        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    unittest.main()
