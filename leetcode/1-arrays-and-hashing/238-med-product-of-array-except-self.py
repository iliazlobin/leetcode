import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_productExceptSelf_example1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_productExceptSelf_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1] * len(nums)
        leftProduct[0] = nums[0]
        for i in range(1, len(nums) - 1):
            leftProduct[i] = leftProduct[i - 1] * nums[i]
        rightProduct = [1] * len(nums)
        rightProduct[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = rightProduct[i + 1] * nums[i]
        for i in range(0, len(nums)):
            left = leftProduct[i - 1] if i > 0 else 1
            right = rightProduct[i + 1] if i < len(nums) - 1 else 1
            nums[i] = left * right
        return nums


if __name__ == "__main__":
    unittest.main()
