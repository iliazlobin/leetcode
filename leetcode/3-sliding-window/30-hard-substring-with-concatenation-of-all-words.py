import enum
import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findSubstring(self):
        # s = "barfoothefoobarman"
        # words = ["foo", "bar"]
        # expected = [0, 9]
        # self.assertEqual(
        #     self.solution.findSubstring(s, words), expected, "Example 1 failed"
        # )

        # s = "wordgoodgoodgoodbestword"
        # words = ["word", "good", "best", "word"]
        # expected = []
        # self.assertEqual(
        #     self.solution.findSubstring(s, words), expected, "Example 2 failed"
        # )

        # s = "barfoofoobarthefoobarman"
        # words = ["bar", "foo", "the"]
        # expected = [6, 9, 12]
        # self.assertEqual(
        #     self.solution.findSubstring(s, words), expected, "Example 3 failed"
        # )

        # s = "wordgoodgoodgoodbestword"
        # words = ["word", "good", "best", "good"]
        # expected = [8]
        # self.assertEqual(
        #     self.solution.findSubstring(s, words),
        #     expected,
        #     "Failed for input: s='wordgoodgoodgoodbestword', words=['word','good','best','good']",
        # )

        s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
        words = ["fooo", "barr", "wing", "ding", "wing"]
        expected = [13]
        self.assertEqual(
            self.solution.findSubstring(s, words),
            expected,
            "Failed for input: s='lingmindraboofooowingdingbarrwingmonkeypoundcake', words=['fooo','barr','wing','ding','wing']",
        )


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        L = len(words[0])
        N = len(words)
        splits = [s[i : i + L] for i in range(0, len(s), L)]

        origs = {}
        for w in words:
            origs[w] = origs.get(w, 0) + 1

        indexes = []  # [(1, 1), (0, 1), (-1, 0), (0, 1), (1, 1), (-1, 0)]
        for part in splits:
            found = False
            for r, w in enumerate(iterable=words):
                if part == w:
                    indexes.append((r, origs[w]))
                    found = True
                    break
            if not found:
                indexes.append((-1, 0))

        res = []
        nWords = {}
        matches = 0
        l = 0
        for r in range(len(indexes)):
            if indexes[r][0] >= 0:
                nWords[indexes[r][0]] = nWords.get(indexes[r][0], 0) + 1
                if nWords[indexes[r][0]] == indexes[r][1]:
                    matches += 1
                elif nWords[indexes[r][0]] == indexes[r][1] + 1:
                    matches -= 1

            if r >= N:
                if indexes[l][0] >= 0:
                    nWords[indexes[l][0]] -= 1
                    if nWords[indexes[l][0]] == indexes[l][1]:
                        matches += 1
                    elif nWords[indexes[l][0]] + 1 == indexes[l][1]:
                        matches -= 1
                l += 1

            if matches == len(origs):
                res.append(l * L)

        return res


if __name__ == "__main__":
    unittest.main()
