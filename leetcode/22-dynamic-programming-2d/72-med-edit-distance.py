import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minDistance(self):
        self.assertEqual(
            self.solution.minDistance("horse", "ros"), 3, "Example 1 failed"
        )
        self.assertEqual(
            self.solution.minDistance("intention", "execution"), 5, "Example 2 failed"
        )
        self.assertEqual(
            self.solution.minDistance("", "a"), 1, "Edge case with empty word1 failed"
        )
        self.assertEqual(
            self.solution.minDistance("a", ""), 1, "Edge case with empty word1 failed"
        )
        self.assertEqual(
            self.solution.minDistance("zoologicoarchaeologist", "zoogeologist"),
            10,
            "Complex case failed",
        )
        self.assertEqual(
            self.solution.minDistance("neatcdee", "neetcode"),
            3,
            "Test case with word1='neatcdee' and word2='neetcode' failed",
        )


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(word2) and i == len(word1):
                return 0
            if i == len(word1):
                return 1 + dfs(i, j + 1)
            elif j == len(word2):
                return 1 + dfs(i + 1, j)

            cache[(i, j)] = 0
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))

            return cache[(i, j)]

        return dfs(0, 0)


class ISolution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for r in range(len(word2) + 1):
            cache[len(word1)][r] = len(word2) - r

        for r in range(len(word1) - 1, -1, -1):
            cache[r][len(word2)] = len(word1) - r
            for c in range(len(word2) - 1, -1, -1):
                if word1[r] == word2[c]:
                    cache[r][c] = cache[r + 1][c + 1]
                else:
                    cache[r][c] = 1 + min(
                        cache[r + 1][c], cache[r][c + 1], cache[r + 1][c + 1]
                    )

        return cache[0][0]


if __name__ == "__main__":
    unittest.main()
