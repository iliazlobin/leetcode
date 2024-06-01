from turtle import back
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permute(self):
        result = self.solution.permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(len(result), len(expected))
        for permutation in result:
            self.assertIn(permutation, expected)

        result = self.solution.permute([0, 1])
        expected = [[0, 1], [1, 0]]
        self.assertEqual(len(result), len(expected))
        for permutation in result:
            self.assertIn(permutation, expected)

        result = self.solution.permute([1])
        expected = [[1]]
        self.assertEqual(result, expected)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        res = []
        for i in nums:
            n = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
            res.extend(perms)
            nums.append(n)

        return res


if __name__ == "__main__":
    unittest.main()
