import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeDuplicates_example1(self):
        nums = [1, 1, 1, 2, 2, 3]
        expected_output = 5
        expected_nums = [1, 1, 2, 2, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output)
        self.assertEqual(nums[:k], expected_nums)

    def test_removeDuplicates_example2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected_output = 7
        expected_nums = [0, 0, 1, 1, 2, 3, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output)
        self.assertEqual(nums[:k], expected_nums)

    def test_removeDuplicates_custom(self):
        nums = [1, 1, 1, 2, 2, 3]
        expected_output = 5
        expected_nums = [1, 1, 2, 2, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output)
        self.assertEqual(nums[:k], expected_nums)

    def test_removeDuplicates_custom(self):
        nums = [1, 1, 1, 2, 2, 2, 3, 3]
        expected_output = 6
        expected_nums = [1, 1, 2, 2, 3, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, expected_output)
        self.assertEqual(nums[:k], expected_nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        for i in range(2, len(nums)):
            # [1, 1, 1, 2, 2, 2, 3, 3]
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j


class SSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        r = 0
        l = -1
        prev = -1
        while r < len(nums):
            if nums[r] != prev:
                count = 0
            if l > 0 and count < 1:
                nums[l] = nums[r]
                l += 1
            if nums[r] == prev:
                count += 1
                if count == 2:
                    if l == -1:
                        l = r
            prev = nums[r]
            r += 1
        return l if l >= 0 else r


if __name__ == "__main__":
    unittest.main()
