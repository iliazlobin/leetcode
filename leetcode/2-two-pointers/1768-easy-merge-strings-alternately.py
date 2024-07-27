import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mergeAlternately_example1(self):
        word1 = "abc"
        word2 = "pqr"
        expected_output = "apbqcr"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), expected_output)

    def test_mergeAlternately_example2(self):
        word1 = "ab"
        word2 = "pqrs"
        expected_output = "apbqrs"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), expected_output)

    def test_mergeAlternately_example3(self):
        word1 = "abcd"
        word2 = "pq"
        expected_output = "apbqcd"
        self.assertEqual(self.solution.mergeAlternately(word1, word2), expected_output)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i1, i2 = 0, 0
        while i1 < len(word1) or i2 < len(word2):
            c1 = word1[i1] if i1 < len(word1) else ""
            c2 = word2[i2] if i2 < len(word2) else ""
            res += c1 + c2
            i1 += 1
            i2 += 1
        return res


if __name__ == "__main__":
    unittest.main()
