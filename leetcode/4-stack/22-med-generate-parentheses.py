from turtle import back
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate_parentheses(self):
        self.assertCountEqual(
            self.solution.generateParentheses(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )
        self.assertCountEqual(self.solution.generateParentheses(1), ["()"])


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res


if __name__ == "__main__":
    unittest.main()
