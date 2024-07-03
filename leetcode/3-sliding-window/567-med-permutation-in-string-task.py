import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_checkInclusion(self):
        self.assertTrue(self.solution.checkInclusion("ab", "sdba"))
        self.assertTrue(self.solution.checkInclusion("ab", "baq"))
        self.assertFalse(self.solution.checkInclusion("ab", "eidboaoo"))
        self.assertFalse(self.solution.checkInclusion("hello", "ooolleoooleh"))
        self.assertTrue(self.solution.checkInclusion("abc", "bbbca"))
        s1 = "abc"
        s2 = "lecaabee"
        expected = False
        self.assertEqual(
            self.solution.checkInclusion(s1, s2),
            expected,
            f"Failed for input: s1='{s1}', s2='{s2}'",
        )


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return None


if __name__ == "__main__":
    unittest.main()
