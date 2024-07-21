import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeKdigits_example1(self):
        self.assertEqual(self.solution.removeKdigits("1432219", 3), "1219")

    def test_removeKdigits_example2(self):
        self.assertEqual(self.solution.removeKdigits("10200", 1), "200")

    def test_removeKdigits_example3(self):
        self.assertEqual(self.solution.removeKdigits("10", 2), "0")


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0:
            stack.pop()
            k -= 1
        while stack and stack[0] == "0":
            stack.popleft()
        return "".join(stack) if len(stack) > 0 else "0"


if __name__ == "__main__":
    unittest.main()
