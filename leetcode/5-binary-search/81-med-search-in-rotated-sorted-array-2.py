import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search_example1(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 0
        expected_output = True
        self.assertEqual(self.solution.search(nums, target), expected_output)

    def test_search_example2(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 3
        expected_output = False
        self.assertEqual(self.solution.search(nums, target), expected_output)

    def test_search_additional(self):
        nums = [1, 0, 1, 1, 1]
        target = 0
        expected_output = True
        self.assertEqual(self.solution.search(nums, target), expected_output)

    def test_search_specific_case(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 13
        expected_output = True
        self.assertEqual(self.solution.search(nums, target), expected_output)


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return True
            elif nums[m] > nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] == nums[m]:
                    l += 1
                elif nums[r] == nums[m]:
                    r -= 1
        return False


if __name__ == "__main__":
    unittest.main()
