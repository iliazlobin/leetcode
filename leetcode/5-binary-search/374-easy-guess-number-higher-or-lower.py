import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_guessNumber_example1(self):
        global pick
        pick = 6
        n = 10
        expected_output = 6
        self.assertEqual(self.solution.guessNumber(n), expected_output)

    def test_guessNumber_example2(self):
        global pick
        pick = 1
        n = 1
        expected_output = 1
        self.assertEqual(self.solution.guessNumber(n), expected_output)

    def test_guessNumber_example3(self):
        global pick
        pick = 1
        n = 2
        expected_output = 1
        self.assertEqual(self.solution.guessNumber(n), expected_output)

    def test_guessNumber_example4(self):
        global pick
        pick = 3
        n = 3
        expected_output = 3
        self.assertEqual(self.solution.guessNumber(n), expected_output)


def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            p = (l + r) // 2
            out = guess(p)
            # if out == 0:
            #     return p
            if out > 0:
                l = p + 1
            elif out <= 0:
                r = p - 1
        return l


if __name__ == "__main__":
    unittest.main()
