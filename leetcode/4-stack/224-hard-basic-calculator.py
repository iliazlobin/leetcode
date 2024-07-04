import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_calculate(self):
        # Example 1
        s = "1 + 1"
        expected = 2
        self.assertEqual(
            self.solution.calculate(s), expected, "Failed for Example 1: s = '1 + 1'"
        )

        # Example 2
        s = " 2-1 + 2 "
        expected = 3
        self.assertEqual(
            self.solution.calculate(s),
            expected,
            "Failed for Example 2: s = ' 2-1 + 2 '",
        )

        # Example 3
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        self.assertEqual(
            self.solution.calculate(s),
            expected,
            "Failed for Example 3: s = '(1+(4+5+2)-3)+(6+8)'",
        )


class Solution:
    def calculate(self, s: str) -> int:
        output, currNum, sign, stack = 0, 0, 1, []

        for char in s:
            if char.isdigit():
                currNum = (currNum * 10) + int(char)
            elif char in "+-":
                output += currNum * sign
                currNum = 0
                if char == "+":
                    sign = 1
                else:
                    sign = -1
            elif char == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                currNum = 0
                sign = 1
            elif char == ")":
                output += currNum * sign
                output *= stack.pop()
                output += stack.pop()
                currNum = 0
                sign = 1

        return output + (currNum * sign)


if __name__ == "__main__":
    unittest.main()
