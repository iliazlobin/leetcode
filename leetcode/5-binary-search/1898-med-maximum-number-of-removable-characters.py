import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maximumRemovals_example1(self):
        s = "abcacb"
        p = "ab"
        removable = [3, 1, 0]
        expected_output = 2
        self.assertEqual(
            self.solution.maximumRemovals(s, p, removable), expected_output
        )

    def test_maximumRemovals_example2(self):
        s = "abcbddddd"
        p = "abcd"
        removable = [3, 2, 1, 4, 5, 6]
        expected_output = 1
        self.assertEqual(
            self.solution.maximumRemovals(s, p, removable), expected_output
        )

    def test_maximumRemovals_example3(self):
        s = "abcab"
        p = "abc"
        removable = [0, 1, 2, 3, 4]
        expected_output = 0
        self.assertEqual(
            self.solution.maximumRemovals(s, p, removable), expected_output
        )

    def test_maximumRemovals_specific_case(self):
        s = "qlevcvgzfpryiqlwy"
        p = "qlecfqlw"
        removable = [12, 5]
        expected_output = 2
        self.assertEqual(
            self.solution.maximumRemovals(s, p, removable), expected_output
        )


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubs(removed):
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i not in removed:
                    if s[i] == p[j]:
                        j += 1
                i += 1
            return j == len(p)

        res = 0
        l, r = 0, len(removable) - 1
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[: m + 1])
            if isSubs(removed):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1

        return res


if __name__ == "__main__":
    unittest.main()
