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

    def test_checkValidString_custom(self):
        s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
        self.assertTrue(self.solution.checkValidString(s), "Expected output is True.")


class Solution:
    def checkValidString(self, s: str) -> bool:
        minB, maxB = 0, 0

        for c in s:
            if c == "(":
                minB += 1
                maxB += 1
            elif c == "*":
                minB -= 1
                maxB += 1
            else:
                minB -= 1
                maxB -= 1

            if minB < 0:
                minB = 0
            if maxB < 0:
                return False

        return minB == 0


if __name__ == "__main__":
    unittest.main()
