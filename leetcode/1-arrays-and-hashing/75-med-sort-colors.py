import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortColors_example1(self):
        nums = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(
            expected, nums, f"Failed on Example 1 with {nums} != {expected}"
        )

    def test_sortColors_example2(self):
        nums = [2, 0, 1]
        expected = [0, 1, 2]
        self.solution.sortColors(nums)
        self.assertEqual(
            expected, nums, f"Failed on Example 2 with {nums} != {expected}"
        )


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, l, r = 0, 0, len(nums) - 1
        # [2, 0, 2, 1, 1, 0]
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1


class BSolution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0] * 3
        for n in nums:
            buckets[n] += 1
        j = 0
        for i in range(len(nums)):
            while buckets[j] == 0:
                j += 1
            nums[i] = j
            buckets[j] -= 1
        return nums


if __name__ == "__main__":
    unittest.main()
