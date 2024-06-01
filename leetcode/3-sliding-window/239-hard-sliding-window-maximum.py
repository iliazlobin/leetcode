import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxSlidingWindow(self):
        self.assertEqual(
            self.solution.maxSlidingWindow([1, 1, 1, 1, 1, 1, 1, 4, 5], 6),
            [3, 3, 5, 5, 6, 7],
        )
        self.assertEqual(
            self.solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7],
        )
        self.assertEqual(self.solution.maxSlidingWindow([1], 1), [1])


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output


if __name__ == "__main__":
    unittest.main()
