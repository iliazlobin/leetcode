import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canJump(self):
        nums = [1, 2, 0, 1, 0]
        result = self.solution.canJump(nums)
        self.assertTrue(result)

        nums = [1, 2, 1, 0, 1]
        result = self.solution.canJump(nums)
        self.assertFalse(result)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        e = len(nums) - 1
        p = e - 1
        while True:
            if p < 0:
                return False
            if nums[p] >= e - p:
                e = p
                p = e - 1
                if e == 0:
                    return True
                continue
            p -= 1


class NeetCodeSolution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


if __name__ == "__main__":
    unittest.main()
