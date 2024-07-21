import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_winnerOfGame_example1(self):
        colors = "AAABABB"
        expected = True
        result = self.solution.winnerOfGame(colors)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_winnerOfGame_example2(self):
        colors = "AA"
        expected = False
        result = self.solution.winnerOfGame(colors)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_winnerOfGame_example3(self):
        colors = "ABBBBBBBAAA"
        expected = False
        result = self.solution.winnerOfGame(colors)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        p = ""
        count = 1
        aTurns = 0
        bTurns = 0
        for c in colors:
            if p == c:
                count += 1
                if count > 2:
                    if c == "A":
                        aTurns += 1
                    else:
                        bTurns += 1
            else:
                count = 1
            p = c
        return aTurns > bTurns


if __name__ == "__main__":
    unittest.main()
