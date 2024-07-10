import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isAnagram(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(self.solution.isAnagram(s, t), True)

        s = "rat"
        t = "car"
        self.assertEqual(self.solution.isAnagram(s, t), False)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


if __name__ == "__main__":
    unittest.main()
