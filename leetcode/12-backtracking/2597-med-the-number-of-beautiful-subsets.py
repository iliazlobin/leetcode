import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_beautifulSubsets_example1(self):
        nums = [2, 4, 6]
        k = 2
        expected = 4
        result = self.solution.beautifulSubsets(nums, k)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_beautifulSubsets_example2(self):
        nums = [1]
        k = 1
        expected = 1
        result = self.solution.beautifulSubsets(nums, k)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_beautifulSubsets_customTest(self):
        nums = [10, 4, 5, 7, 2, 1]
        k = 3
        expected = 23
        result = self.solution.beautifulSubsets(nums, k)
        self.assertEqual(
            expected,
            result,
            f"Failed with nums={nums} and k={k} where expected {expected} but got {result}",
        )


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = {}

        def dfs(i):
            if i == len(nums):
                return 1

            res = dfs(i + 1)
            if (nums[i] + k not in count or count[nums[i] + k] == 0) and (
                nums[i] - k not in count or count[nums[i] - k] == 0
            ):
                count[nums[i]] = count.get(nums[i], 0) + 1
                res += dfs(i + 1)
                count[nums[i]] -= 1
            return res

        return dfs(0) - 1


class XSolution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i, count):
            if i == len(nums):
                return 1

            res = dfs(i + 1, count)
            # if nums[i] + k not in count and nums[i] - k not in count:
            if not count[nums[i] + k] and not count[nums[i] - k]:
                count[nums[i]] += 1
                res += dfs(i + 1, count)
                count[nums[i]] -= 1
            return res

        return dfs(0, defaultdict(int)) - 1


if __name__ == "__main__":
    unittest.main()
