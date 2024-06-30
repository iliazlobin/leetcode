import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_change(self):
        self.assertEqual(self.solution.change(5, [1, 2, 5]), 4, "Example 1 failed")
        self.assertEqual(self.solution.change(3, [2]), 0, "Example 2 failed")
        self.assertEqual(self.solution.change(10, [10]), 1, "Example 3 failed")


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache: List[List[int]] = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        cache[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1, 1):
            for i in range(len(coins) - 1, -1, -1):
                cache[a][i] = cache[a][i + 1]
                if a - coins[i] >= 0:
                    cache[a][i] += cache[a - coins[i]][i]

        return cache[amount][0]


class CSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return cache[(i, total)]

        return dfs(0, 0)


class RSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0

        def dfs(i, total):
            nonlocal res

            if i == len(coins):
                return
            if total > amount:
                return
            if total == amount:
                res += 1
                return
            for j in range(i, len(coins), 1):
                dfs(j, total + coins[j])

        dfs(0, 0)
        return res


if __name__ == "__main__":
    unittest.main()
