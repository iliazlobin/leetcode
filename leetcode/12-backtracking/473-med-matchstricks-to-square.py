import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_makesquare_example1(self):
        matchsticks = [1, 1, 2, 2, 2]
        expected = True
        result = self.solution.makesquare(matchsticks)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_makesquare_example2(self):
        matchsticks = [3, 3, 3, 3, 4]
        expected = False
        result = self.solution.makesquare(matchsticks)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        length = int(sum(matchsticks) / 4)
        sides = [0] * 4

        matchsticks.sort(reverse=True)

        def dfs(i) -> None | bool:
            if i == len(matchsticks):
                # for j in range(4):
                #     if sides[j] == length:
                #         return True
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]

            return False

        return dfs(0)


if __name__ == "__main__":
    unittest.main()
