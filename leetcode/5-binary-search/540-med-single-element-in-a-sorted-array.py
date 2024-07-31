import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_singleNonDuplicate_example1(self):
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        expected_output = 2
        self.assertEqual(self.solution.singleNonDuplicate(nums), expected_output)

    def test_singleNonDuplicate_example2(self):
        nums = [3, 3, 7, 7, 10, 11, 11]
        expected_output = 10
        self.assertEqual(self.solution.singleNonDuplicate(nums), expected_output)


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if (m > 0 and m % 2 != 0 and nums[m] == nums[m - 1]) or (
                m < len(nums) - 1 and m % 2 == 0 and nums[m] == nums[m + 1]
            ):
                l = m + 1
            else:
                r = m - 1
        return nums[l]


if __name__ == "__main__":
    unittest.main()
