import enum
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sumSubarrayMins_example1(self):
        self.assertEqual(
            self.solution.sumSubarrayMins([3, 1, 2, 4]),
            17,
            "The sum of subarray minimums does not match the expected output.",
        )

    def test_sumSubarrayMins_example2(self):
        self.assertEqual(
            self.solution.sumSubarrayMins([11, 81, 94, 43, 3]),
            444,
            "The sum of subarray minimums does not match the expected output.",
        )


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        res = [0] * len(arr)
        stack = [0]
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            res[i] = res[stack[-1]] + (i - stack[-1]) * arr[i]
            stack.append(i)
        return sum(res) % (10**9 + 7)


class RSolution:  # Time limit
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        res = 0
        stack = []

        def dfs(i):
            nonlocal res

            if i == len(arr):
                if stack:
                    m = stack[0][0]
                    for v in stack:
                        m = min(m, v[0])
                    res += m
                return

            if not stack or stack and i - stack[-1][1] == 1:
                stack.append((arr[i], i))
                dfs(i + 1)
                stack.pop()
            dfs(i + 1)

        dfs(0)
        return res


if __name__ == "__main__":
    unittest.main()
