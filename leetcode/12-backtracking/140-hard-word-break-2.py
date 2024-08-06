import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_wordBreak_example1(self):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        expected_output = ["cats and dog", "cat sand dog"]
        self.assertEqual(
            sorted(self.solution.wordBreak(s, wordDict)), sorted(expected_output)
        )

    def test_wordBreak_example2(self):
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        expected_output = [
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple",
        ]
        self.assertEqual(
            sorted(self.solution.wordBreak(s, wordDict)), sorted(expected_output)
        )

    def test_wordBreak_example3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        expected_output = []
        self.assertEqual(self.solution.wordBreak(s, wordDict), expected_output)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]
        wordsSet = set()
        for w in wordDict:
            wordsSet.add(w)
        res = []

        def dfs(i, words):
            if i == len(s):
                res.append(" ".join(words))
                return

            for j in range(i + 1, len(s) + 1):
                w = s[i:j]
                if w not in wordsSet:
                    continue
                dfs(j, words + [w])

        dfs(0, [])
        return res


if __name__ == "__main__":
    unittest.main()
