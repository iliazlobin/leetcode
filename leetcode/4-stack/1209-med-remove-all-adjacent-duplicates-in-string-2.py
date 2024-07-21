import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeDuplicates_example1(self):
        self.assertEqual(self.solution.removeDuplicates("abcd", 2), "abcd")

    def test_removeDuplicates_example2(self):
        self.assertEqual(self.solution.removeDuplicates("deeedbbcccbdaa", 3), "aa")

    def test_removeDuplicates_example3(self):
        self.assertEqual(
            self.solution.removeDuplicates("pbbcggttciiippooaais", 2), "ps"
        )

    def test_removeDuplicates_additional(self):
        self.assertEqual(
            self.solution.removeDuplicates(
                "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4
            ),
            "ybth",
        )


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            count = 1
            if stack and stack[-1][0] == c:
                count = stack[-1][1] + 1

            stack.append((c, count))

            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()

        return "".join([c for c, _ in stack])


if __name__ == "__main__":
    unittest.main()
