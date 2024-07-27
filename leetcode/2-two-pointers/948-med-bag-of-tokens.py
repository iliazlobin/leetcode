import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_bagOfTokensScore_example1(self):
        tokens = [100]
        power = 50
        expected_output = 0
        self.assertEqual(self.solution.bagOfTokensScore(tokens, power), expected_output)

    def test_bagOfTokensScore_example2(self):
        tokens = [200, 100]
        power = 150
        expected_output = 1
        self.assertEqual(self.solution.bagOfTokensScore(tokens, power), expected_output)

    def test_bagOfTokensScore_example3(self):
        tokens = [100, 200, 300, 400]
        power = 200
        expected_output = 2
        self.assertEqual(self.solution.bagOfTokensScore(tokens, power), expected_output)

    def test_bagOfTokensScore_example4(self):
        tokens = [26]
        power = 51
        expected_output = 1
        self.assertEqual(self.solution.bagOfTokensScore(tokens, power), expected_output)

    def test_bagOfTokensScore_example5(self):
        tokens = [71, 55, 82]
        power = 54
        expected_output = 0
        self.assertEqual(self.solution.bagOfTokensScore(tokens, power), expected_output)


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        res = 0
        while True:
            while l < len(tokens) and power >= tokens[l] and l <= r:
                power -= tokens[l]
                l += 1
                res += 1
            if l == 0 or l >= r:
                break
            power += tokens[r]
            r -= 1
            res -= 1
        return res


if __name__ == "__main__":
    unittest.main()
