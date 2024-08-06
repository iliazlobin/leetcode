import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxScoreWords_example1(self):
        words = ["dog", "cat", "dad", "good"]
        # words = ["dad", "good"]
        letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
        score = [
            1,
            0,
            9,
            5,
            0,
            0,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
        expected_output = 23
        self.assertEqual(
            self.solution.maxScoreWords(words, letters, score), expected_output
        )

    # def test_maxScoreWords_example2(self):
    #     words = ["xxxz", "ax", "bx", "cx"]
    #     letters = ["z", "a", "b", "c", "x", "x", "x"]
    #     score = [
    #         4,
    #         4,
    #         4,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         5,
    #         0,
    #         10,
    #     ]
    #     expected_output = 27
    #     self.assertEqual(
    #         self.solution.maxScoreWords(words, letters, score), expected_output
    #     )

    # def test_maxScoreWords_example3(self):
    #     words = ["leetcode"]
    #     letters = ["l", "e", "t", "c", "o", "d"]
    #     score = [
    #         0,
    #         0,
    #         1,
    #         1,
    #         1,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         1,
    #         0,
    #         0,
    #         1,
    #         0,
    #         0,
    #         0,
    #         0,
    #         1,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #     ]
    #     expected_output = 0
    #     self.assertEqual(
    #         self.solution.maxScoreWords(words, letters, score), expected_output
    #     )


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        scores = {chr(ord("a") + i): s for i, s in enumerate(score)}
        letterCount = Counter(letters)

        def canFormWord(wordCount):
            for c in wordCount:
                if wordCount[c] > letterCount[c]:
                    return False
            return True

        res = 0
        def dfs(w, score):
            nonlocal res

            if w == len(words):
                return

            dfs(w + 1, score)

            wordCount = Counter(words[w])
            if canFormWord(wordCount):
                for c in wordCount:
                    letterCount[c] -= wordCount[c]
                    score += scores[c] * wordCount[c]
                res = max(res, score)
                dfs(w + 1, score)
                for c in wordCount:
                    letterCount[c] += wordCount[c]
                    score -= scores[c] * wordCount[c]

        dfs(0, 0)
        return res


if __name__ == "__main__":
    unittest.main()
