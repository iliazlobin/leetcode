import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expectedNums = [2, 2]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertEqual(sorted(nums[:k]), sorted(expectedNums))

    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expectedNums = [0, 1, 3, 0, 4]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertEqual(sorted(nums[:k]), sorted(expectedNums))

    def test_no_removal(self):
        nums = [1, 2, 3, 4, 5]
        val = 6
        expectedNums = [1, 2, 3, 4, 5]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertEqual(sorted(nums[:k]), sorted(expectedNums))

    def test_all_elements_removed(self):
        nums = [1, 1, 1, 1]
        val = 1
        expectedNums = []
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertEqual(sorted(nums[:k]), sorted(expectedNums))

    def test_mixed_elements(self):
        nums = [4, 5, 4, 6, 4, 7]
        val = 4
        expectedNums = [5, 6, 7]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertEqual(sorted(nums[:k]), sorted(expectedNums))


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        # [1, 2, 3, 4, 5] val=6
        while l <= r:
            if nums[l] != val:
                l += 1
                continue
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
                r -= 1
            else:
                r -= 1
        return l

if __name__ == "__main__":
    unittest.main()
