import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "aba"
        expected = True
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "abca"
        expected = True
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)

    def test_example3(self):
        s = "abc"
        expected = False
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "a"
        expected = True
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)

    def test_two_characters(self):
        s = "ab"
        expected = True
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)

    def test_long_palindrome(self):
        s = "deeee"
        expected = True
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)

    def test_custom_case(self):
        s = "eeccccbebaeeabebccceea"
        expected = False
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)

    def test_cbbcc(self):
        s = "cbbcc"
        expected = True
        result = self.solution.validPalindrome(s)
        self.assertEqual(result, expected)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        left = -1
        right = -1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif left == -1:
                left = l
                right = r
                l += 1
            elif right >= 0:
                l = left
                r = right - 1
                right = -1
            else:
                return False
        return True


if __name__ == "__main__":
    unittest.main()
