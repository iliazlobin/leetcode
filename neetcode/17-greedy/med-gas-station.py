import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        # self.solution = NeetCodeSolution()

    def test_canCompleteCircuit(self):
        gas = [1, 2, 3, 4]
        cost = [2, 2, 4, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        self.assertEqual(result, 3)

        gas = [1, 2, 3]
        cost = [2, 3, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        self.assertEqual(result, -1)

        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        self.assertEqual(result, 3)

        gas = [5, 8, 2, 8]
        cost = [6, 5, 6, 6]
        result = self.solution.canCompleteCircuit(gas, cost)
        self.assertEqual(result, 3)

        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        self.assertEqual(result, 4)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        dif = []
        for i in range(0, len(gas)):
            dif.append(gas[i] - cost[i])

        balance = 0
        balance_i = 0
        for i, d in enumerate(dif):
            balance += d
            if balance < 0:
                balance = 0
                balance_i = i + 1

        return balance_i


class NeetCodeSolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1

        return res


if __name__ == "__main__":
    unittest.main()
