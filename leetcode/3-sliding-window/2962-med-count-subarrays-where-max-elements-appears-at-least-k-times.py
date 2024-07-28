import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countSubarrays_example1(self):
        nums = [1, 3, 2, 3, 3]
        k = 2
        expected_output = 6
        self.assertEqual(self.solution.countSubarrays(nums, k), expected_output)

    def test_countSubarrays_example2(self):
        nums = [1, 4, 2, 1]
        k = 3
        expected_output = 0
        self.assertEqual(self.solution.countSubarrays(nums, k), expected_output)


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        l = 0
        count = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == target:
                count += 1
            while count == k:
                res += len(nums) - r
                if nums[l] == target:
                    count -= 1
                l += 1
        return res


if __name__ == "__main__":
    unittest.main()
