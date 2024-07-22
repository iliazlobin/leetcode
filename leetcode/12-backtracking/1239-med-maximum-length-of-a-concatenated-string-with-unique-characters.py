import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxLength_example1(self):
        arr = ["un", "iq", "ue"]
        expected = 4
        result = self.solution.maxLength(arr)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_maxLength_example2(self):
        arr = ["cha", "r", "act", "ers"]
        expected = 6
        result = self.solution.maxLength(arr)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_maxLength_example3(self):
        arr = ["abcdefghijklmnopqrstuvwxyz"]
        expected = 26
        result = self.solution.maxLength(arr)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()
        res = 0

        def dfs(i, ss):
            nonlocal res

            if i == len(arr):
                res = max(res, len(ss))
                return

            valid = True
            curSet = set()
            for c in arr[i]:
                if c in curSet:
                    valid = False
                curSet.add(c)
                if c in charSet:
                    valid = False
                    break
            if valid:
                for c in arr[i]:
                    charSet.add(c)
                dfs(i + 1, ss + arr[i])
                for c in arr[i]:
                    if c in charSet:
                        charSet.remove(c)

            dfs(i + 1, ss)

        dfs(0, "")
        return res


if __name__ == "__main__":
    unittest.main()
