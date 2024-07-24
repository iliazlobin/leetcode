import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "fl")

    def test_example2(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_single_string(self):
        strs = ["single"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "single")

    def test_empty_string(self):
        strs = [""]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_no_common_prefix(self):
        strs = ["abc", "def", "ghi"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_all_strings_same(self):
        strs = ["same", "same", "same"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "same")


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        c = ""
        while i < len(strs[0]):
            for j, s in enumerate(strs):
                if j == 0:
                    c = s[i]
                elif i == len(s) or s[i] != c:
                    return strs[0][:i]
            i += 1
            if i == len(strs[0]):
                break
        return strs[0]


if __name__ == "__main__":
    unittest.main()
