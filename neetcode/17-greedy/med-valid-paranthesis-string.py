import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_checkValidString(self):
        s = "((**)"
        result = self.solution.checkValidString(s)
        self.assertTrue(result)

        s = "(((*)"
        result = self.solution.checkValidString(s)
        self.assertFalse(result)

        s = "(*))"
        result = self.solution.checkValidString(s)
        self.assertTrue(result)


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for l in s:
            if l == "(":
                leftMin += 1
                leftMax += 1
            elif l == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMax += 1
                leftMin -= 1
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False
        return leftMin == 0

if __name__ == "__main__":
    unittest.main()
