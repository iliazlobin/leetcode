import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_backspaceCompare_example1(self):
        s = "ab#c"
        t = "ad#c"
        expected_output = True
        self.assertEqual(self.solution.backspaceCompare(s, t), expected_output)

    def test_backspaceCompare_example2(self):
        s = "ab##"
        t = "c#d#"
        expected_output = True
        self.assertEqual(self.solution.backspaceCompare(s, t), expected_output)

    def test_backspaceCompare_example3(self):
        s = "a#c"
        t = "b"
        expected_output = False
        self.assertEqual(self.solution.backspaceCompare(s, t), expected_output)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        for c in s:
            if c == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c)
        stackT = []
        for c in t:
            if c == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c)
        if len(stackS) != len(stackT):
            return False
        for i in range(len(stackS)):
            if stackS[i] != stackT[i]:
                return False
        return True


if __name__ == "__main__":
    unittest.main()
