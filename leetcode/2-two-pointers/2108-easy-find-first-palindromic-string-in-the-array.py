import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_firstPalindrome_example1(self):
        words = ["abc", "car", "ada", "racecar", "cool"]
        expected_output = "ada"
        self.assertEqual(self.solution.firstPalindrome(words), expected_output)

    def test_firstPalindrome_example2(self):
        words = ["notapalindrome", "racecar"]
        expected_output = "racecar"
        self.assertEqual(self.solution.firstPalindrome(words), expected_output)

    def test_firstPalindrome_example3(self):
        words = ["def", "ghi"]
        expected_output = ""
        self.assertEqual(self.solution.firstPalindrome(words), expected_output)


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                return words[i]
        return ""


if __name__ == "__main__":
    unittest.main()
