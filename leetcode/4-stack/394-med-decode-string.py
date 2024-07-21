from curses.ascii import isdigit
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_decodeString_example1(self):
        self.assertEqual(self.solution.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_decodeString_example2(self):
        self.assertEqual(self.solution.decodeString("3[a2[c]]"), "accaccacc")

    def test_decodeString_example3(self):
        self.assertEqual(self.solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c == "]":
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)

                for c in sub * num:
                    stack.append(c)

                continue

            stack.append(c)

        return "".join(stack)


if __name__ == "__main__":
    unittest.main()
