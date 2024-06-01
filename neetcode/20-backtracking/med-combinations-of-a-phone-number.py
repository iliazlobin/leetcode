from unicodedata import digit
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_letterCombinations(self):
        # digits = "34"
        # result = self.solution.letterCombinations(digits)
        # self.assertEqual(
        #     sorted(result),
        #     sorted(["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]),
        # )

        digits = ""
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, [])


class Solution:
    digitsMap = {
        "0": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        def dfs(i, cur):
            if len(cur) == len(digits) and cur != "":
                res.append(cur)
            if i == len(digits):
                return
            for c in self.digitsMap[digits[i]]:
                dfs(i + 1, cur + c)
        
        dfs(0, "")
        return res

if __name__ == "__main__":
    unittest.main()
