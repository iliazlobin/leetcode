import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_wordBreak(self):
        self.assertTrue(
            self.solution.wordBreak("leetcode", ["leet", "code"]), "Example 1 failed"
        )
        self.assertTrue(
            self.solution.wordBreak("applepenapple", ["apple", "pen"]),
            "Example 2 failed",
        )
        self.assertFalse(
            self.solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]),
            "Example 3 failed",
        )


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


if __name__ == "__main__":
    unittest.main()
