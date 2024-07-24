import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = NCSolution()

    def test_twoSum(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if n in diffs:
                return [i, diffs[n]]
            diffs[diff] = i
        return []


class SSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if not j > i:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class NCSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i


if __name__ == "__main__":
    unittest.main()
