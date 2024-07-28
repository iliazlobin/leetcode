import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValid(self):
        print()

    def test_minOperations_example1(self):
        nums = [1, 1, 4, 2, 3]
        x = 5
        expected_output = 2
        self.assertEqual(self.solution.minOperations(nums, x), expected_output)

    def test_minOperations_example2(self):
        nums = [5, 6, 7, 8, 9]
        x = 4
        expected_output = -1
        self.assertEqual(self.solution.minOperations(nums, x), expected_output)

    def test_minOperations_example3(self):
        nums = [3, 2, 20, 1, 1, 3]
        x = 10
        expected_output = 5
        self.assertEqual(self.solution.minOperations(nums, x), expected_output)


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        total = 0
        res = -1
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            while total > target and l <= r:
                total -= nums[l]
                l += 1

            if total == target:
                res = max(res, r - l + 1)

        return len(nums) - res if res != -1 else -1


if __name__ == "__main__":
    unittest.main()
