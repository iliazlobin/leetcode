import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rotate_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected_output = [5, 6, 7, 1, 2, 3, 4]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected_output)

    def test_rotate_example2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected_output = [3, 99, -1, -100]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected_output)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        offset = k % len(nums)
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, len(nums) - 1)
        reverse(0, offset - 1)
        reverse(offset, len(nums) - 1)

class SSolution:
    def rotate(self, nums: List[int], k: int) -> None:
        offset = k % len(nums)
        if offset == 0:
            return nums

        res = [0] * len(nums)
        j = 0
        for i in range(offset, len(nums)):
            res[i] = nums[j]
            j += 1
        for i in range(0, offset):
            res[i] = nums[j]
            j += 1

        for i, c in enumerate(res):
            nums[i] = c


if __name__ == "__main__":
    unittest.main()
