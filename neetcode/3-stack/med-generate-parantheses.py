import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = NeetCodeSolution()
        self.solution = Solution()

    def test_generateParenthesis(self):
        # result = self.solution.generateParenthesis(1)
        # self.assertEqual(result, ["()"])

        result = self.solution.generateParenthesis(3)
        expected_result = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(set(result), set(expected_result))
        # In the official solution, order matters
        # self.assertEqual(result, expected_result)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = self.generate(n)
        return res

    def generate(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        nested = self.generate(n - 1)
        aggregate = []
        for a in nested:
            left = f"(){a}"
            right = f"{a}()"
            aggregate.append(left)
            if left != right:
                aggregate.append(right)
            aggregate.append(f"({a})")

        return aggregate


class NeetCodeSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


if __name__ == "__main__":
    unittest.main()
