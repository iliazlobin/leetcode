import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_evalRPN_examples(self):
        tokens1 = ["2", "1", "+", "3", "*"]
        self.assertEqual(
            self.solution.evalRPN(tokens1), 9, "Failed for input: {}".format(tokens1)
        )

        tokens2 = ["4", "13", "5", "/", "+"]
        self.assertEqual(
            self.solution.evalRPN(tokens2), 6, "Failed for input: {}".format(tokens2)
        )

        tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(
            self.solution.evalRPN(tokens3), 22, "Failed for input: {}".format(tokens3)
        )

        tokens = ["0", "3", "/"]
        self.assertEqual(
            self.solution.evalRPN(tokens), 0, "Failed for input: {}".format(tokens)
        )


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["-", "+", "*", "/"]
        operatorsFuncs = {
            "-": lambda a, b: int(a) - int(b),
            "+": lambda a, b: int(a) + int(b),
            "*": lambda a, b: int(a) * int(b),
            "/": lambda a, b: int(int(a) / int(b)),
        }
        for t in tokens:
            if t not in operators:
                stack.append(t)
                continue
            right = int(stack.pop())
            left = int(stack.pop())
            result = operatorsFuncs[t](left, right)
            stack.append(result)
        return int(stack[0])


if __name__ == "__main__":
    unittest.main()
