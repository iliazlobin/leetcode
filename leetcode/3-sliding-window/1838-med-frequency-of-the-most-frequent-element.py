import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxFrequency_example1(self):
        nums = [1, 2, 4]
        k = 5
        expected_output = 3
        self.assertEqual(self.solution.maxFrequency(nums, k), expected_output)

    def test_maxFrequency_example2(self):
        nums = [1, 4, 8, 13]
        k = 5
        expected_output = 2
        self.assertEqual(self.solution.maxFrequency(nums, k), expected_output)

    def test_maxFrequency_example3(self):
        nums = [3, 9, 6]
        k = 2
        expected_output = 1
        self.assertEqual(self.solution.maxFrequency(nums, k), expected_output)


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        l = 0
        res = 0
        # [13, 8, 4, 1]
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            fill = nums[l] * (r - l + 1)
            if fill - total > k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    unittest.main()
