import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortedSquares_example1(self):
        nums = [-4, -1, 0, 3, 10]
        expected_output = [0, 1, 9, 16, 100]
        self.assertEqual(self.solution.sortedSquares(nums), expected_output)

    def test_sortedSquares_example2(self):
        nums = [-7, -3, 2, 3, 11]
        expected_output = [4, 9, 9, 49, 121]
        self.assertEqual(self.solution.sortedSquares(nums), expected_output)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            nums[i] = n * n
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        j = len(res) - 1
        while l <= r:
            if nums[l] > nums[r]:
                res[j] = nums[l]
                l += 1
            else:
                res[j] = nums[r]
                r -= 1
            j -= 1
        return res


if __name__ == "__main__":
    unittest.main()
