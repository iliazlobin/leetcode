from turtle import back
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate_parentheses(self):
        self.assertCountEqual(
            self.solution.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )
        self.assertCountEqual(self.solution.generateParenthesis(1), ["()"])

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, sub):
            if open == close == n:
                res.append(sub)
                return
            
            if open < n:
                dfs(open + 1, close, sub + "(")
            if close < open:
                dfs(open, close + 1, sub + ")")
            
        dfs(0, 0, "")
        return res

class SSolution:
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
