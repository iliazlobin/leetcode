import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        s = "1 + 1"
        expected = 2
        self.assertEqual(
            self.solution.calculate(s), expected, "Failed for Example 1: s = '1 + 1'"
        )

    def test_case_2(self):
        s = " 2-1 + 2 "
        expected = 3
        self.assertEqual(
            self.solution.calculate(s),
            expected,
            "Failed for Example 2: s = ' 2-1 + 2 '",
        )

    def test_case_3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        self.assertEqual(
            self.solution.calculate(s),
            expected,
            "Failed for Example 3: s = '(1+(4+5+2)-3)+(6+8)'",
        )

    def test_case_4(self):
        s = "2147483647"
        expected = 2147483647
        self.assertEqual(
            self.solution.calculate(s),
            expected,
            "Failed for s = '2147483647'",
        )


class Solution:
    def calculate(self, s: str) -> int:
        num, output, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                output += num * sign
                num = 0
                if c == "+":
                    sign = 1
                else:
                    sign = -1
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ")":
                output += num * sign
                output *= stack.pop()
                output += stack.pop()
                num = 0
                sign = 0
        return output + num * sign


if __name__ == "__main__":
    unittest.main()
