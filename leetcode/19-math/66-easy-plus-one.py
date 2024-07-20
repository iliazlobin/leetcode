import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_plusOne(self):
        self.assertEqual(
            self.solution.plusOne([1, 2, 3]), [1, 2, 4], "Should be [1, 2, 4]"
        )
        self.assertEqual(
            self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2], "Should be [4, 3, 2, 2]"
        )
        self.assertEqual(self.solution.plusOne([9]), [1, 0], "Should be [1, 0]")


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    unittest.main()
