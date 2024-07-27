import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findContentChildren_example1(self):
        g = [1, 2, 3]
        s = [1, 1]
        expected_output = 1
        self.assertEqual(self.solution.findContentChildren(g, s), expected_output)

    def test_findContentChildren_example2(self):
        g = [1, 2]
        s = [1, 2, 3]
        expected_output = 2
        self.assertEqual(self.solution.findContentChildren(g, s), expected_output)


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        c = 0
        i = 0
        while i < len(g):
            while c < len(s) and s[c] < g[i]:
                c += 1
            if c == len(s):
                break
            c += 1
            i += 1

        return i


if __name__ == "__main__":
    unittest.main()
