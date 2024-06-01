import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = OnSolution()

    def test_maxSubArray(self):
        nums = [2, -3, 4, -2, 2, 1, -1, 4]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 8)

        nums = [-1]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, -1)

        nums = [-2, 1]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 1)


class On3Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        m = float("-inf")
        for i in range(0, len(nums)):
            for j in range(0, i + 1):
                s = 0
                for k in range(j, i + 1):
                    s += nums[k]
                m = max(m, s)
        return m


class On2Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        m = float("-inf")
        for i in range(0, len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                m = max(m, s)
        return m


class OnSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        return max_sub


if __name__ == "__main__":
    unittest.main()
