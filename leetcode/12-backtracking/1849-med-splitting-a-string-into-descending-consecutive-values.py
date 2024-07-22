import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_splitString_example1(self):
        s = "1234"
        expected = False
        result = self.solution.splitString(s)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_splitString_example2(self):
        s = "050043"
        expected = True
        result = self.solution.splitString(s)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_splitString_example3(self):
        s = "9080701"
        expected = False
        result = self.solution.splitString(s)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )

    def test_splitString_input10(self):
        s = "10"
        expected = True
        result = self.solution.splitString(s)
        self.assertEqual(expected, result, f"Failed with input {s} where expected {expected} but got {result}")

class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i, prev):
            if i == len(s):
                return True

            # 9080701
            for j in range(i + 1, len(s) + 1):
                ss = s[i:j]
                n = int(ss)
                if prev == 0 or (prev > 0 and prev - 1 == n):
                    if dfs(j, n):
                        return (prev == 0 and i == 0 and j != len(s)) or prev != 0

            return False

        return dfs(0, 0)


if __name__ == "__main__":
    unittest.main()
