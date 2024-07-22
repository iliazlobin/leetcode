import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subarraySum_example1(self):
        nums = [1, 1, 1]
        k = 2
        expected = 2
        result = self.solution.subarraySum(nums, k)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_subarraySum_example2(self):
        nums = [1, 2, 3]
        k = 3
        expected = 2
        result = self.solution.subarraySum(nums, k)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_subarraySum_customTest(self):
        nums = [-1, -1, 1]
        k = 0
        expected = 1
        result = self.solution.subarraySum(nums, k)
        self.assertEqual(
            expected,
            result,
            f"Failed with nums={nums} and k={k} where expected {expected} but got {result}",
        )

    def test_subarraySum_customTest2(self):
        nums = [1, 2, 1, 2, 1]
        k = 3
        expected = 4
        result = self.solution.subarraySum(nums, k)
        self.assertEqual(
            expected,
            result,
            f"Failed with nums={nums} and k={k} where expected {expected} but got {result}",
        )


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {0 : 1}
        total = 0
        for n in nums:
            total += n
            if total - k in prefixSum:
                res += prefixSum[total - k]
            prefixSum[total] = prefixSum.get(total, 0) + 1
        return res


if __name__ == "__main__":
    unittest.main()
