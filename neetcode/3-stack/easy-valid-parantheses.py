import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValid(self):
        s = "[]"
        result = self.solution.isValid(s)
        self.assertEqual(result, True)

        s = "([{}])"
        result = self.solution.isValid(s)
        self.assertEqual(result, True)

        s = "[(])"
        result = self.solution.isValid(s)
        self.assertEqual(result, False)

        s = "]"
        result = self.solution.isValid(s)
        self.assertEqual(result, False)


class Solution:
    open_pair = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    close_brackets = [")", "]", "}"]

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # is close bracket
            if c in self.close_brackets:
                if not stack:
                    return False
                last = stack.pop()
                if last not in self.open_pair:
                    return False
                close_bracket = self.open_pair[last]
                if c != close_bracket:
                    return False
            # is open bracket
            elif c in self.open_pair:
                stack.append(c)
        if stack:
            return False
        return True


class DraftSolution:
    open_pair = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    # close_pair = {
    #     ")": "(",
    #     "]": "[",
    #     "}": "{",
    # }
    close_brackets = [")", "]", "}"]

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # is close bracket
            if c in self.close_brackets:
                last = stack.pop()
                if last not in self.open_pair:
                    return False
                close_bracket = self.open_pair[last]
                if c != close_bracket:
                    return False
            # is open bracket
            elif c in self.open_pair:
                stack.append(c)
        if stack:
            return False
        return True


if __name__ == "__main__":
    unittest.main()
