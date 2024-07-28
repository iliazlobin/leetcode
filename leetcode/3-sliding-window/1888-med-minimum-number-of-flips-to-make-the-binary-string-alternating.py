import itertools
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minFlips_example1(self):
        s = "111000"
        expected_output = 2
        self.assertEqual(self.solution.minFlips(s), expected_output)

    def test_minFlips_example2(self):
        s = "010"
        expected_output = 0
        self.assertEqual(self.solution.minFlips(s), expected_output)

    def test_minFlips_example3(self):
        s = "1110"
        expected_output = 1
        self.assertEqual(self.solution.minFlips(s), expected_output)


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        l, r = 0, 0
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"

        res = len(s)
        diff1, diff2 = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            if r - l + 1 > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
        return res


class SSolution:
    def minFlips(self, s: str) -> int:
        l, r = 0, 0
        diffs1, diffs2 = 0, 0
        val1, val2 = "1", "0"
        res = float("inf")
        while r < len(s) + len(s) - 1:
            c = s[r] if r < len(s) else s[r - len(s)]
            if c != val1:
                diffs1 += 1
            if c != val2:
                diffs2 += 1
            if r - l + 1 > len(s):
                v = s[l]
                beg1 = val1 if len(s) % 2 != 0 else self.opposite(val1)
                beg2 = val2 if len(s) % 2 != 0 else self.opposite(val2)
                if v != beg1:
                    diffs1 -= 1
                if v != beg2:
                    diffs2 -= 1
                res = min(res, diffs1, diffs2)
                l += 1
            r += 1
            val1 = self.opposite(val1)
            val2 = self.opposite(val2)
        return res

    def opposite(self, v):
        return "1" if v == "0" else "0"


class LSolution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        change_count = sum(int(ch) != (i & 1) for i, ch in enumerate(s))

        if n & 1 == 0: 
            if 2*change_count > len(s):
                change_count = n-change_count
        else:
            count = min_count = change_count
            for ch, ch0 in zip(s, itertools.cycle("01")): 
                count += 1 if ch==ch0 else -1
                if count < change_count:
                    change_count = count
                elif n - count < change_count:
                    change_count = n - count

        return change_count

if __name__ == "__main__":
    unittest.main()
