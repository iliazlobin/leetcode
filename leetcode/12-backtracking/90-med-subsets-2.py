from turtle import back
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsetsWithDup(self):
        result = self.solution.subsetsWithDup([1, 2, 2])
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        self.assertEqual(len(result), len(expected))
        for subset in result:
            self.assertIn(Counter(subset), map(Counter, expected))

        result = self.solution.subsetsWithDup([0])
        expected = [[], [0]]
        self.assertEqual(len(result), len(expected))
        for subset in result:
            self.assertIn(Counter(subset), map(Counter, expected))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        array = []

        def backtrack(i):
            if i == len(nums):
                res.append(array.copy())
                return

            array.append(nums[i])
            backtrack(i + 1)
            array.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res


if __name__ == "__main__":
    unittest.main()
