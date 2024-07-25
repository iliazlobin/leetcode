import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_arrayStringsAreEqual_example1(self):
        word1 = ["ab", "c"]
        word2 = ["a", "bc"]
        result = self.solution.arrayStringsAreEqual(word1, word2)
        self.assertTrue(result)

    def test_arrayStringsAreEqual_example2(self):
        word1 = ["a", "cb"]
        word2 = ["ab", "c"]
        result = self.solution.arrayStringsAreEqual(word1, word2)
        self.assertFalse(result)

    def test_arrayStringsAreEqual_example3(self):
        word1 = ["abc", "d", "defg"]
        word2 = ["abcddefg"]
        result = self.solution.arrayStringsAreEqual(word1, word2)
        self.assertTrue(result)

    def test_arrayStringsAreEqual_custom(self):
        word1 = ["abc", "d", "defg"]
        word2 = ["abcddef"]
        result = self.solution.arrayStringsAreEqual(word1, word2)
        self.assertFalse(result)


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1, e1, i2, e2 = 0, 0, 0, 0
        while True:
            if word1[i1][e1] != word2[i2][e2]:
                return False
            e1 += 1
            while i1 < len(word1) and e1 == len(word1[i1]):
                if e1 == len(word1[i1]):
                    e1 = 0
                i1 += 1
            e2 += 1
            while i2 < len(word2) and e2 == len(word2[i2]):
                if e2 == len(word2[i2]):
                    e2 = 0
                i2 += 1
            if i1 == len(word1) or i2 == len(word2):
                return i1 == len(word1) and i2 == len(word2)


if __name__ == "__main__":
    unittest.main()
