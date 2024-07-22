import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsetXORSum_example1(self):
        nums = [1, 3]
        expected = 6
        result = self.solution.subsetXORSum(nums)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_subsetXORSum_example2(self):
        nums = [5, 1, 6]
        expected = 28
        result = self.solution.subsetXORSum(nums)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_subsetXORSum_example3(self):
        nums = [3, 4, 5, 6, 7, 8]
        expected = 480
        result = self.solution.subsetXORSum(nums)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(i, xor):
            nonlocal res

            if i == len(nums):
                res += xor
                return

            dfs(i + 1, xor)
            dfs(i + 1, xor ^ nums[i])

        dfs(0, 0)
        return res


if __name__ == "__main__":
    unittest.main()
