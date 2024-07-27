import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kthGrammar_example1(self):
        n = 1
        k = 1
        expected_output = 0
        self.assertEqual(self.solution.kthGrammar(n, k), expected_output)

    def test_kthGrammar_example2(self):
        n = 2
        k = 1
        expected_output = 0
        self.assertEqual(self.solution.kthGrammar(n, k), expected_output)

    def test_kthGrammar_example3(self):
        n = 2
        k = 2
        expected_output = 1
        self.assertEqual(self.solution.kthGrammar(n, k), expected_output)


# 0
# 01
# 0110
# 01101001
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        res = 0
        l, r = 0, 2 ** (n - 1)
        for _ in range(n - 1):
            m  = (l + r) // 2
            if k <= m:
                r = m
            else:
                l = m + 1
                res = 1 if res == 0 else 1
        return res


if __name__ == "__main__":
    unittest.main()
