import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numberOfBeams_example1(self):
        bank = ["011001", "000000", "010100", "001000"]
        expected = 8
        result = self.solution.numberOfBeams(bank)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_numberOfBeams_example2(self):
        bank = ["000", "111", "000"]
        expected = 0
        result = self.solution.numberOfBeams(bank)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []
        for r in bank:
            count = 0
            for c in r:
                if c == "1":
                    count += 1
            devices.append(count)
        prev = 0
        res = 0
        for d in devices:
            if d != 0:
                if prev == 0:
                    prev = d
                else:
                    res += prev * d
                    prev = d
        return res


if __name__ == "__main__":
    unittest.main()
