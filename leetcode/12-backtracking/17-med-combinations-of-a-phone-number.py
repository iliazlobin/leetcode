import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_letterCombinations(self):
        self.assertEqual(
            sorted(self.solution.letterCombinations("23")),
            sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        )
        self.assertEqual(self.solution.letterCombinations(""), [])
        self.assertEqual(
            sorted(self.solution.letterCombinations("2")), sorted(["a", "b", "c"])
        )


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
