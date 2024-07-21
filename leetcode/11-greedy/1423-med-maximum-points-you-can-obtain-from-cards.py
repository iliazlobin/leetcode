import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxScore_example1(self):
        self.assertEqual(
            self.solution.maxScore([1, 2, 3, 4, 5, 6, 1], 3), 12, "Example 1 failed."
        )

    def test_maxScore_example2(self):
        self.assertEqual(self.solution.maxScore([2, 2, 2], 2), 4, "Example 2 failed.")

    def test_maxScore_example3(self):
        self.assertEqual(
            self.solution.maxScore([9, 7, 7, 9, 7, 7, 9], 7), 55, "Example 3 failed."
        )

    def test_maxScore_custom1(self):
        self.assertEqual(
            self.solution.maxScore([100, 40, 17, 9, 73, 75], 3),
            248,
            "Custom test case failed.",
        )


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        winSize = len(cardPoints) - k
        totalSum = sum(cardPoints)
        if winSize == 0:
            return totalSum

        globalMinSum = float("inf")
        localSum = 0
        for i in range(len(cardPoints)):
            localSum += cardPoints[i]
            if i + 1 >= winSize:
                globalMinSum = min(globalMinSum, localSum)
                localSum -= cardPoints[i + 1 - winSize]

        return totalSum - globalMinSum


if __name__ == "__main__":
    unittest.main()
