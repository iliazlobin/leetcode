import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverseWords(self):
        self.assertEqual(
            self.solution.reverseWords("the sky is blue"),
            "blue is sky the",
            "Example 1 failed",
        )

        self.assertEqual(
            self.solution.reverseWords("  hello world  "),
            "world hello",
            "Example 2 failed",
        )

        self.assertEqual(
            self.solution.reverseWords("a good   example"),
            "example good a",
            "Example 3 failed",
        )


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        out = ""
        for i in range(len(words) - 1, 0, -1):
            out += words[i] + " "
        out += words[0]
        return out


if __name__ == "__main__":
    unittest.main()
