import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numSubseq_example1(self):
        nums = [3, 5, 6, 7]
        target = 9
        expected_output = 4
        self.assertEqual(self.solution.numSubseq(nums, target), expected_output)

    def test_numSubseq_example2(self):
        nums = [3, 3, 6, 8]
        target = 10
        expected_output = 6
        self.assertEqual(self.solution.numSubseq(nums, target), expected_output)

    def test_numSubseq_example3(self):
        nums = [2, 3, 3, 4, 6, 7]
        target = 12
        expected_output = 61
        self.assertEqual(self.solution.numSubseq(nums, target), expected_output)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()

        r = len(nums) - 1
        for i, l in enumerate(nums):
            while (l + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                res += 2 ** (r - i)
                res %= 10**9 + 7
        return res


if __name__ == "__main__":
    unittest.main()
