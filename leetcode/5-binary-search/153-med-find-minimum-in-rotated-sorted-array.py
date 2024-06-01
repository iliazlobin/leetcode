import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMin(self):
        nums = [3, 4, 5, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 1)

        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 0)

        nums = [11, 13, 15, 17]
        self.assertEqual(self.solution.findMin(nums), 11)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res


if __name__ == "__main__":
    unittest.main()
