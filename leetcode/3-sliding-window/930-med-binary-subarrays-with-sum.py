import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numSubarraysWithSum_example1(self):
        nums = [1, 0, 1, 0, 1]
        goal = 2
        expected_output = 4
        self.assertEqual(self.solution.numSubarraysWithSum(nums, goal), expected_output)

    def test_numSubarraysWithSum_example2(self):
        nums = [0, 0, 0, 0, 0]
        goal = 0
        expected_output = 15
        self.assertEqual(self.solution.numSubarraysWithSum(nums, goal), expected_output)


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def process(g):
            if g < 0:
                return 0
            res = 0
            l = 0
            total = 0
            res = 0
            for r in range(len(nums)):
                total += nums[r]
                while total > g:
                    total -= nums[l]
                    l += 1
                res += r - l + 1
            return res

        return process(goal) - process(goal - 1)


if __name__ == "__main__":
    unittest.main()
