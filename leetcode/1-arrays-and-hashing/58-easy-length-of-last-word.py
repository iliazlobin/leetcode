import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "Hello World"
        self.assertEqual(self.solution.lengthOfLastWord(s), 5)

    def test_example2(self):
        s = "   fly me   to   the moon  "
        self.assertEqual(self.solution.lengthOfLastWord(s), 4)

    def test_example3(self):
        s = "luffy is still joyboy"
        self.assertEqual(self.solution.lengthOfLastWord(s), 6)

    def test_single_word(self):
        s = "word"
        self.assertEqual(self.solution.lengthOfLastWord(s), 4)

    def test_trailing_spaces(self):
        s = "a "
        self.assertEqual(self.solution.lengthOfLastWord(s), 1)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if length > 0 and s[i] != " ":
                length += 1
            elif length == 0 and s[i] != " ":
                length = 1
            elif length > 0 and s[i] == " ":
                break
        return length


if __name__ == "__main__":
    unittest.main()
