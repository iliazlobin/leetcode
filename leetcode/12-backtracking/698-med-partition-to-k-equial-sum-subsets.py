import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canPartitionKSubsets_example1(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_canPartitionKSubsets_example2(self):
        nums = [1, 2, 3, 4]
        k = 3
        expected = False
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_canPartitionKSubsets_newTest(self):
        nums = [2, 2, 2, 2, 3, 4, 5]
        k = 4
        expected = False
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(
            expected,
            result,
            f"Failed with nums={nums} and k={k} where expected {expected} but got {result}",
        )


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = int(sum(nums) / k)

        used = [False] * len(nums)

        # [4, 3, 2, 3, 5, 2, 1]
        # k = 4, target = 5
        def dfs(i, k, cur):
            if k == 0:
                return True
            if cur == target:
                return dfs(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or cur + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j + 1, k, cur + nums[j]):
                    return True
                used[j] = False
            return False

        return dfs(0, k, 0)


class XSolution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = int(sum(nums) / k)

        buckets = [0] * k

        # [4, 3, 2, 3, 5, 2, 1]
        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    buckets[j] -= nums[i]

            return False

        return dfs(0)


if __name__ == "__main__":
    unittest.main()
