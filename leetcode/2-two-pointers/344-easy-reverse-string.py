import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverseString_example1(self):
        s = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_reverseString_example2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["h", "a", "n", "n", "a", "H"])

    def test_reverseString_example3(self):
        s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"])


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


if __name__ == "__main__":
    unittest.main()
