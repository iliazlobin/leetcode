import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):
        numbers = [1, 2, 3, 4]
        target = 3
        res = self.solution.twoSum(numbers, target)
        self.assertEqual(res, [0, 1])

        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

        nums = [2, 7, 11, 15]
        target = 9
        res = self.solution.twoSum(nums, target)
        self.assertEqual(res, [0, 1])


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            for ii, nn in enumerate(numbers):
                if ii <= i:
                    continue
                if n + nn == target:
                    return [i, ii]
        return []


if __name__ == "__main__":
    unittest.main()
