import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestConsecutive(self):
        # nums = [100, 4, 200, 1, 3, 2]
        # self.assertEqual(self.solution.longestConsecutive(nums), 4)

        # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        # self.assertEqual(self.solution.longestConsecutive(nums), 9)

        # nums = [0]
        # self.assertEqual(self.solution.longestConsecutive(nums), 1)

        nums = [1, 2, 0, 1]
        self.assertEqual(self.solution.longestConsecutive(nums), 3)


# O(logN*n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        maxS = 1
        curS = 0
        for i, n in enumerate(nums):
            if i > 0 and n - 1 == nums[i - 1]:
                curS += 1
                maxS = max(maxS, curS + 1)
            elif i > 0 and n > nums[i - 1]:
                curS = 0

        return maxS


if __name__ == "__main__":
    unittest.main()
