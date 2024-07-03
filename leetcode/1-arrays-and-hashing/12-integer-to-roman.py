import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intToRoman(self):
        self.assertEqual(
            self.solution.intToRoman(3749), "MMMDCCXLIX", "Example 1 failed"
        )

        self.assertEqual(self.solution.intToRoman(58), "LVIII", "Example 2 failed")

        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV", "Example 3 failed")


class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        res = ""
        while num > 0:
            for key in sorted(romans.keys(), reverse=True):
                count = num // key
                res += romans[key] * count
                num -= key * count

        return res

if __name__ == "__main__":
    unittest.main()
