import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permute(self):
        nums = [1, 2, 3]
        result = self.solution.permute(nums)
        self.assertEqual(
            sorted(result),
            sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        )

        nums = [7]
        result = self.solution.permute(nums)
        self.assertEqual(result, [[7]])


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)

            res.extend(perms)

            nums.append(n)

        return res


if __name__ == "__main__":
    unittest.main()
