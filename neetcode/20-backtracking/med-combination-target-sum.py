import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combinationSum(self):
        nums = [2, 5, 6, 9]
        target = 9
        result = self.solution.combinationSum(nums, target)
        self.assertEqual(sorted(result), sorted([[2, 2, 5], [9]]))

        nums = [3, 4, 5]
        target = 16
        result = self.solution.combinationSum(nums, target)
        self.assertEqual(
            sorted(result),
            sorted([[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]),
        )

        nums = [3]
        target = 5
        result = self.solution.combinationSum(nums, target)
        self.assertEqual(result, [])


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur: list, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    unittest.main()
