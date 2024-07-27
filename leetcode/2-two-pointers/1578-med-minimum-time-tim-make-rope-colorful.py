import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minCost_example1(self):
        colors = "abaac"
        neededTime = [1, 2, 3, 4, 5]
        expected_output = 3
        self.assertEqual(self.solution.minCost(colors, neededTime), expected_output)

    def test_minCost_example2(self):
        colors = "abc"
        neededTime = [1, 2, 3]
        expected_output = 0
        self.assertEqual(self.solution.minCost(colors, neededTime), expected_output)

    def test_minCost_example3(self):
        colors = "aabaa"
        neededTime = [1, 2, 3, 4, 1]
        expected_output = 2
        self.assertEqual(self.solution.minCost(colors, neededTime), expected_output)


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        maxTime = neededTime[0]
        totalTime = neededTime[0]
        for i in range(len(colors)):
            if i > 0:
                if colors[i] == colors[i - 1]:
                    maxTime = max(maxTime, neededTime[i])
                    totalTime += neededTime[i]
                else:
                    if totalTime > maxTime:
                        res += totalTime - maxTime
                    maxTime = neededTime[i]
                    totalTime = neededTime[i]
        if totalTime > maxTime:
            res += totalTime - maxTime
        return res


class NSolution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
        return res


if __name__ == "__main__":
    unittest.main()
