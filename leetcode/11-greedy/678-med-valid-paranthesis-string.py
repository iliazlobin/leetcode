import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_checkValidString(self):
        # Example 1
        s = "()"
        self.assertTrue(
            self.solution.checkValidString(s), "Failed for Example 1: s = '()'"
        )

        # Example 2
        s = "(*)"
        self.assertTrue(
            self.solution.checkValidString(s), "Failed for Example 2: s = '(*)'"
        )

        # Example 3
        s = "(*))"
        self.assertTrue(
            self.solution.checkValidString(s), "Failed for Example 3: s = '(*))'"
        )

        s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
        self.assertTrue(
            self.solution.checkValidString(s),
            "Failed for custom case: s = '((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()'",
        )


class Solution:
    def checkValidString(self, s: str) -> bool:
        minBrackets = 0
        maxBrackets = 0

        for c in s:
            if c == "(":
                minBrackets += 1
                maxBrackets += 1
            elif c == "*":
                minBrackets -= 1
                maxBrackets += 1
            else:
                minBrackets -= 1
                maxBrackets -= 1

            if maxBrackets < 0:
                return False
            if minBrackets < 0:
                minBrackets = 0

        return minBrackets == 0


if __name__ == "__main__":
    unittest.main()
