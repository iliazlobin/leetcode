import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minSubArrayLen_example1(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        expected_output = 2
        self.assertEqual(self.solution.minSubArrayLen(target, nums), expected_output)

    def test_minSubArrayLen_example2(self):
        target = 4
        nums = [1, 4, 4]
        expected_output = 1
        self.assertEqual(self.solution.minSubArrayLen(target, nums), expected_output)

    def test_minSubArrayLen_example3(self):
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        expected_output = 0
        self.assertEqual(self.solution.minSubArrayLen(target, nums), expected_output)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("inf")
        # [2, 3, 1, 2, 4, 3]
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float("inf") else 0


if __name__ == "__main__":
    unittest.main()
