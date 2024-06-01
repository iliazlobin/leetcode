import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_jump(self):
        nums = [2, 4, 1, 1, 1, 1]
        result = self.solution.jump(nums)
        self.assertEqual(result, 2)

        nums = [2, 1, 2, 1, 0]
        result = self.solution.jump(nums)
        self.assertEqual(result, 2)


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i])
            l = r + 1
            r = r + farthest
            res += 1

        return res


if __name__ == "__main__":
    unittest.main()
