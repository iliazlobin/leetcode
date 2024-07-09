import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getMaxAdditionalDinersCount(self):
        self.assertEqual(self.solution.getMaxAdditionalDinersCount(10, 1, 2, [2, 6]), 3)
        self.assertEqual(
            self.solution.getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]), 1
        )


class XSolution:
    def getMaxAdditionalDinersCount(self, N: int, K: int, M: int, S: List[int]) -> int:
        res = 0
        i = 1
        while i < N + 1:
            overlap = False
            for s in S:
                sl = s - K
                sr = s + K
                if i >= sl and i <= sr:
                    overlap = True
                    break
            if overlap:
                i = sr + 1
            else:
                res += 1
                i = i + K + 1
        return res

class Solution:
    def getMaxAdditionalDinersCount(self, N: int, K: int, M: int, S: List[int]):
        S.sort()  # Sort the current diners' positions
        additional_diners = 0  # Initialize the count of additional diners

        # Calculate the potential spots before the first diner
        if S[0] - K - 1 > 0:
            additional_diners += (S[0] - K - 1) // (K + 1)

        # Calculate the potential spots between diners
        for i in range(1, M):
            distance = S[i] - S[i-1] - 2*K - 1  # Distance between diners minus the exclusion zones
            if distance > 0:
                additional_diners += distance // (K + 1)

        # Calculate the potential spots after the last diner
        if N - S[-1] - K > 0:
            additional_diners += (N - S[-1] - K) // (K + 1)

        return additional_diners

if __name__ == "__main__":
    unittest.main()
