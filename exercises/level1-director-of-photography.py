import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_artisticPhotograph(self):
        self.assertEqual(self.solution.getArtisticPhotographCount(5, "APABA", 1, 2), 1)
        self.assertEqual(self.solution.getArtisticPhotographCount(5, "APABA", 2, 3), 0)
        self.assertEqual(
            self.solution.getArtisticPhotographCount(8, ".PBAAP.B", 1, 3), 3
        )


class XSolution:
    def getArtisticPhotographCount(self, N: int, C: str, X: int, Y: int) -> int:
        if N < 2:
            return 0
        l, c, r = 0, 1, 2

        res = 0
        while r < N:
            if C[c] == "A":
                if (C[l] == "P" and (c - l) >= X and (c - l) <= Y) and (
                    C[r] == "B" and (r - c) >= X and (r - c) <= Y
                ):
                    res += 1
            if c + 1 < r and r - c >= X and r - c <= Y:
                c += 1
            elif l + 1 < c:
                l += 1
            else:
                r += 1

        return res


class Solution:
    def getArtisticPhotographCount(self, N: int, C: str, X: int, Y: int) -> int:
        artistic_photos = 0

        for i in range(N):
            if C[i] == "A":  # Found an actor
                p_left = p_right = b_left = b_right = 0
                # Count photographers and backdrops within the distance constraints
                for dist in range(X, Y + 1):
                    if i - dist >= 0:
                        if C[i - dist] == "P":
                            p_left += 1
                        elif C[i - dist] == "B":
                            b_left += 1
                    if i + dist < N:
                        if C[i + dist] == "P":
                            p_right += 1
                        elif C[i + dist] == "B":
                            b_right += 1
                # Add to total count
                artistic_photos += p_left * b_right + p_right * b_left

        return artistic_photos


if __name__ == "__main__":
    unittest.main()
