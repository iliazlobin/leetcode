import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_convert(self):
        self.assertEqual(
            self.solution.convert("PAYPALISHIRING", 3),
            "PAHNAPLSIIGYIR",
            "Example 1 failed",
        )

        self.assertEqual(
            self.solution.convert("PAYPALISHIRING", 4),
            "PINALSIGYAHRPI",
            "Example 2 failed",
        )

        self.assertEqual(self.solution.convert("A", 1), "A", "Example 3 failed")


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        out = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(s):
                    out += s[j]
                    j += (numRows - 1) * 2
            else:
                j = i
                d = j + (numRows - i - 1) * 2
                while j < len(s) or d < len(s):
                    if j <= d:
                        out += s[j]
                        j += (numRows - 1) * 2
                    else:
                        out += s[d]
                        d += (numRows - 1) * 2
        return out


if __name__ == "__main__":
    unittest.main()
