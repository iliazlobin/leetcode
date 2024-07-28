import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxVowels_example1(self):
        s = "abciiidef"
        k = 3
        expected_output = 3
        self.assertEqual(self.solution.maxVowels(s, k), expected_output)

    def test_maxVowels_example2(self):
        s = "aeiou"
        k = 2
        expected_output = 2
        self.assertEqual(self.solution.maxVowels(s, k), expected_output)

    def test_maxVowels_example3(self):
        s = "leetcode"
        k = 3
        expected_output = 2
        self.assertEqual(self.solution.maxVowels(s, k), expected_output)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        vowelsMap = {v: True for v in vowels}
        count = 0
        res = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in vowelsMap:
                count += 1
            if r - l + 1 > k:
                if s[l] in vowelsMap:
                    count -= 1
                l += 1
            res = max(res, count)
            r += 1
        return res


if __name__ == "__main__":
    unittest.main()
