import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fib_examples(self):
        # Example 1
        self.assertEqual(self.solution.fib(2), 1, "Failed for n=2")

        # Example 2
        self.assertEqual(self.solution.fib(3), 2, "Failed for n=3")

        # Example 3
        self.assertEqual(self.solution.fib(4), 3, "Failed for n=4")


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev = 1
        prev2 = 0
        res = 0
        for _ in range(n - 1):
            res = prev + prev2
            prev2 = prev
            prev = res

        return res


class RSolution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    unittest.main()
