import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition(self):
        result = self.solution.partition("aab")
        expected = [["a", "a", "b"], ["aa", "b"]]
        self.assertEqual(len(result), len(expected))
        for partition in result:
            self.assertIn(partition, expected)

        result = self.solution.partition("a")
        expected = [["a"]]
        self.assertEqual(result, expected)


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, sub):
            if i == len(s):
                res.append(sub.copy())
                return

            for j in range(i, len(s)):
                if isPali(i, j):
                    dfs(j + 1, sub + [s[i : j + 1]])

        dfs(0, [])
        return res


class SSolution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        array = []

        def isPali(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(array.copy())

            for j in range(i, len(s)):
                if isPali(i, j):
                    ss = s[i : j + 1]
                    array.append(ss)
                    dfs(j + 1)
                    array.pop()

        dfs(0)
        return res

if __name__ == "__main__":
    unittest.main()
