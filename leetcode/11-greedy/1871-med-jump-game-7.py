import unittest
from typing import List, Optional
from collections import deque


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canReach_example1(self):
        self.assertTrue(
            self.solution.canReach("011010", 2, 3), "Expected output is True."
        )

    def test_canReach_example2(self):
        self.assertFalse(
            self.solution.canReach("01101110", 2, 3), "Expected output is False."
        )

    def test_canReach_custom(self):
        self.assertFalse(
            self.solution.canReach("00111010", 3, 5), "Expected output is False."
        )


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            k = q.popleft()
            for i in range(
                max(k + minJump, farthest + 1), min(k + maxJump + 1, len(s))
            ):
                if s[i] == "0":
                    if i == len(s) - 1:
                        return True
                    q.append(i)
            farthest = k + maxJump

        return False


if __name__ == "__main__":
    unittest.main()
