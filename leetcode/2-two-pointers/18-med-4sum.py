import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_fourSum_example1(self):
    #     nums = [1, 0, -1, 0, -2, 2]
    #     target = 0
    #     result = self.solution.fourSum(nums, target)
    #     expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    #     self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    # def test_fourSum_example2(self):
    #     nums = [2, 2, 2, 2, 2]
    #     target = 8
    #     result = self.solution.fourSum(nums, target)
    #     expected = [[2, 2, 2, 2]]
    #     self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_fourSum_custom(self):
        nums = [0, 0, 0, 0]
        target = 0
        result = self.solution.fourSum(nums, target)
        expected = [[0, 0, 0, 0]]
        self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        l1, l2 = 0, 1
        res = {}
        while l1 < len(nums) - 3:
            t = target - nums[l1] - nums[l2]

            l, r = l2 + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == t:
                    res[tuple([nums[l1], nums[l2], nums[l], nums[r]])] = True
                    l += 1
                elif s < t:
                    l += 1
                else:
                    r -= 1

            l2 += 1
            if l2 > len(nums) - 3:
                l2 = l1 + 2
                l1 += 1

        return list(res.keys())


if __name__ == "__main__":
    unittest.main()
