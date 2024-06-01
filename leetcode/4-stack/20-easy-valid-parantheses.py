import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValid_examples(self):
        s1 = "()"
        self.assertTrue(self.solution.isValid(s1), f"Failed for input: {s1}")

        s2 = "()[]{}"
        self.assertTrue(self.solution.isValid(s2), f"Failed for input: {s2}")

        s3 = "(]"
        self.assertFalse(self.solution.isValid(s3), f"Failed for input: {s3}")


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in mapping:
                stack.append(c)
                continue
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()

        return not stack


if __name__ == "__main__":
    unittest.main()
