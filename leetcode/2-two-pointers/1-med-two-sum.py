import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum_additional(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(
            self.solution.twoSum(numbers, target), [1, 2], "Example 1 failed"
        )

        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(
            self.solution.twoSum(numbers, target), [1, 3], "Example 2 failed"
        )

        numbers = [-1, 0]
        target = -1
        self.assertEqual(
            self.solution.twoSum(numbers, target), [1, 2], "Example 3 failed"
        )

        numbers = [5, 25, 75]
        target = 100
        expected = [2, 3]
        self.assertEqual(
            self.solution.twoSum(numbers, target),
            expected,
            f"Failed for input: {numbers} with target: {target}",
        )

        numbers = [3, 24, 50, 79, 88, 150, 345]
        target = 200
        expected = [3, 6]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1


class MSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashM = {}

        for i, n in enumerate(numbers):
            if n in hashM:
                return [hashM[n] + 1, i + 1]
            hashM[target - n] = i


class BSolution:
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
