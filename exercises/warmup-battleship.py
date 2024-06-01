import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getHitProbability(self):
        R1, C1 = 2, 3
        G1 = [[0, 0, 1], [1, 0, 1]]
        self.assertAlmostEqual(self.solution.getHitProbability(R1, C1, G1), 0.5)

        R2, C2 = 2, 2
        G2 = [[1, 1], [1, 1]]
        self.assertAlmostEqual(self.solution.getHitProbability(R2, C2, G2), 1.0)


class Solution:
    def getHitProbability(self, R: int, C: int, G: List[List[int]]) -> float:
        ones = 0
        for r in range(len(G)):
            for c in range(len(G[0])):
                if G[r][c] == 1:
                    ones += 1
        return ones / (R * C)


if __name__ == "__main__":
    unittest.main()
