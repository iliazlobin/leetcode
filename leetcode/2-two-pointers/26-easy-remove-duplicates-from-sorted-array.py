import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeDuplicates_example1(self):
        nums = [1, 1, 2]
        expected_output = 2
        expected_nums = [1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output)
        self.assertEqual(nums[:k], expected_nums)

    def test_removeDuplicates_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_output = 5
        expected_nums = [0, 1, 2, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output)
        self.assertEqual(nums[:k], expected_nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = -1
        for r in range(len(nums)):
            if r > 0 and nums[r] == nums[r - 1]:
                if l == -1:
                    l = r
                r += 1
                continue
            if l > 0:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l if l > 0 else len(nums)


if __name__ == "__main__":
    unittest.main()
