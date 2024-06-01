import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getWrongAnswers(self):
        self.assertEqual(self.solution.getWrongAnswers(3, "ABA"), "BAB")
        self.assertEqual(self.solution.getWrongAnswers(5, "BBBBB"), "AAAAA")

class Solution:
    def getWrongAnswers(self, N: int, C: str) -> str:
        switch = {
            "A": "B",
            "B": "A",
        }
        return "".join([switch[char] for char in C])

if __name__ == "__main__":
    unittest.main()
