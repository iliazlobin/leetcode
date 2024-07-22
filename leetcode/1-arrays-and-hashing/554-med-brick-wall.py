import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leastBricks_example1(self):
        wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
        expected = 2
        result = self.solution.leastBricks(wall)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_leastBricks_example2(self):
        wall = [[1], [1], [1]]
        expected = 3
        result = self.solution.leastBricks(wall)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hMap = defaultdict(int)
        maxGaps = 0
        for r in range(len(wall)):
            pos = 0
            for i in range(0, len(wall[r]) - 1):
                pos += wall[r][i]
                hMap[pos] += 1
                maxGaps = max(maxGaps, hMap[pos])
        return len(wall) - maxGaps


if __name__ == "__main__":
    unittest.main()
