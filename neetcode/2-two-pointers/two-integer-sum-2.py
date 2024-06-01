import unittest
from typing import List, Optional

from regex import R


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            for ii, nn in enumerate(numbers):
                if ii <= i:
                    continue
                if n + nn == target:
                    return [i + 1, ii + 1]
        return []

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        numbers = [1,2,3,4]
        target = 3
        result = self.solution.twoSum(numbers, target)
        self.assertEqual(result, [1, 2])

        numbers = [2,3,4]
        target = 6
        result = self.solution.twoSum(numbers, target)
        self.assertEqual(result, [1, 3])

if __name__ == "__main__":
    unittest.main()
