import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverseWords_example1(self):
        s = "Let's take LeetCode contest"
        expected_output = "s'teL ekat edoCteeL tsetnoc"
        self.assertEqual(self.solution.reverseWords(s), expected_output)

    def test_reverseWords_example2(self):
        s = "Mr Ding"
        expected_output = "rM gniD"
        self.assertEqual(self.solution.reverseWords(s), expected_output)


class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        for w in s.split():
            res += w[::-1] + " "
        return res[:-1]


if __name__ == "__main__":
    unittest.main()
