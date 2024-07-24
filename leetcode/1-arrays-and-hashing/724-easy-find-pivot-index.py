import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 7, 3, 6, 5, 6]
        expected = 3
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [1, 2, 3]
        expected = -1
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [2, 1, -1]
        expected = 0
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [1]
        expected = 0
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, expected)

    def test_no_pivot(self):
        nums = [1, 2, 3, 4, 5, 6]
        expected = -1
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, expected)

    def test_custom_case(self):
        nums = [-1, -1, -1, -1, -1, 0]
        expected = 2
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, expected)


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        
        return -1

if __name__ == "__main__":
    unittest.main()
