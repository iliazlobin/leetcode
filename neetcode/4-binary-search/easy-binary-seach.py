import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        nums = [-1, 0, 2, 4, 6, 8]
        target = 4
        result = self.solution.search(nums, target)
        self.assertEqual(result, 3)

        nums = [-1, 0, 2, 4, 6, 8]
        target = 3
        result = self.solution.search(nums, target)
        self.assertEqual(result, -1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target == n:
                return i
        return -1

if __name__ == "__main__":
    unittest.main()

