import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numSubarrayProductLessThanK_example1(self):
        nums = [10, 5, 2, 6]
        k = 100
        expected_output = 8
        self.assertEqual(
            self.solution.numSubarrayProductLessThanK(nums, k), expected_output
        )

    def test_numSubarrayProductLessThanK_example2(self):
        nums = [1, 2, 3]
        k = 0
        expected_output = 0
        self.assertEqual(
            self.solution.numSubarrayProductLessThanK(nums, k), expected_output
        )


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        l = 0
        res = 0
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product /= nums[l]
                l += 1
            res += r - l + 1
        return res


if __name__ == "__main__":
    unittest.main()
