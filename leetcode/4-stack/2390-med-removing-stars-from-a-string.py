import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeStars_example1(self):
        self.assertEqual(self.solution.removeStars("leet**cod*e"), "lecoe")

    def test_removeStars_example2(self):
        self.assertEqual(self.solution.removeStars("erase*****"), "")


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
                continue

            stack.append(c)
        
        return "".join(stack)


if __name__ == "__main__":
    unittest.main()
