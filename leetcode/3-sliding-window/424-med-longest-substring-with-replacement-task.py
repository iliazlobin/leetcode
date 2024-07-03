import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        # self.solution = NSolution()

    def test_characterReplacement(self):
        self.assertEqual(self.solution.characterReplacement("XYYX", 2), 4)
        self.assertEqual(self.solution.characterReplacement("AAABABB", 1), 5)
        self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return None


if __name__ == "__main__":
    unittest.main()
