import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isInterleave(self):
        # self.assertTrue(
        #     self.solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"),
        #     "Example 1 failed",
        # )
        # self.assertFalse(
        #     self.solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"),
        #     "Example 2 failed",
        # )
        # self.assertTrue(self.solution.isInterleave("", "", ""), "Example 3 failed")

        s1 = "aabc"
        s2 = "abad"
        s3 = "aabcabad"
        expected = True
        self.assertEqual(
            self.solution.isInterleave(s1, s2, s3),
            expected,
            f"Failed for input: s1='{s1}', s2='{s2}', s3='{s3}'",
        )


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        cache[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s3[i + j] == s1[i] and cache[i + 1][j]:
                    cache[i][j] = True
                if j < len(s2) and s3[i + j] == s2[j] and cache[i][j + 1]:
                    cache[i][j] = True

        return cache[0][0]


class RSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def backtrack(l, l1, l2):
            if l == len(s3):
                return l1 == len(s1) and l2 == len(s2)

            if l1 < len(s1) and s3[l] == s1[l1]:
                if backtrack(l + 1, l1 + 1, l2):
                    return True
            if l2 < len(s2) and s3[l] == s2[l2]:
                if backtrack(l + 1, l1, l2 + 1):
                    return True

            return False

        return backtrack(0, 0, 0)


if __name__ == "__main__":
    unittest.main()
