import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permuteUnique_example1(self):
        nums = [1, 1, 2]
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        result = self.solution.permuteUnique(nums)
        self.assertEqual(
            len(expected), len(result), "Incorrect number of permutations returned."
        )
        for permutation in expected:
            self.assertIn(
                permutation, result, f"Permutation {permutation} not found in result."
            )

    def test_permuteUnique_example2(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        result = self.solution.permuteUnique(nums)
        self.assertEqual(
            len(expected), len(result), "Incorrect number of permutations returned."
        )
        for permutation in expected:
            self.assertIn(
                permutation, result, f"Permutation {permutation} not found in result."
            )


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        res = []
        perms = []

        def dfs():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            for n in count:
                if count[n] > 0:
                    perms.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perms.pop()

        dfs()
        return res


if __name__ == "__main__":
    unittest.main()
