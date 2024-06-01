import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverseBits(self):
        n = 0b00000000000000000000000000010101
        result = self.solution.reverseBits(n)
        self.assertEqual(result, 0b10101000000000000000000000000000)


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res


if __name__ == "__main__":
    unittest.main()
