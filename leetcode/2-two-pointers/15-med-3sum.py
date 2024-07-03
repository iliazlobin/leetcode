import enum
from multiprocessing import connection
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_threeSum(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = self.solution.threeSum(nums)
        self.assertEqual(
            len(result), len(expected), "Example 1 failed: Incorrect number of results"
        )
        for triplet in expected:
            self.assertIn(triplet, result, f"Example 1 failed: {triplet} not in result")

        nums = [0, 1, 1]
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected, "Example 2 failed")

        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected, "Example 3 failed")

        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.threeSum(nums)
        self.assertEqual(len(result), len(expected), "Failed for input: [0,0,0,0]")
        for triplet in expected:
            self.assertIn(
                triplet,
                result,
                "Failed for input: [0,0,0,0]: Expected triplet not in result",
            )


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1

        return res


if __name__ == "__main__":
    unittest.main()
