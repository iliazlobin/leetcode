import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_evalRPN(self):
        # tokens = ["1", "2", "+", "3", "*", "4", "-"]
        # result = self.solution.evalRPN(tokens)
        # self.assertEqual(result, 5)

        tokens = ["4", "13", "5", "/", "+"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 6)


class Solution:
    operations = ["+", "-", "*", "/"]

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # check if operation
            if t in self.operations:
                right = stack.pop() if stack else None
                left = stack.pop() if stack else None
                if left is None or right is None:
                    raise ValueError("Wrong Polish Expression")
                res = eval(f"{left} {t} {right}")
                stack.append(int(res))
                continue

            # TODO: check for number

            # if len(stack) > 2:
            #     return Exception("Missing operand")

            stack.append(t)

        if len(stack) != 1:
            return Exception("Expression Not Complete")

        final = stack.pop()
        return final


class NeetCodeSolution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]


if __name__ == "__main__":
    unittest.main()
