import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_maxSlidingWindow(self):
    #     # self.assertEqual(
    #     #     self.solution.maxSlidingWindow([1, 1, 1, 1, 1, 1, 1, 4, 5], 6),
    #     #     [3, 3, 5, 5, 6, 7],
    #     # )
    #     self.assertEqual(
    #         self.solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
    #         [3, 3, 5, 5, 6, 7],
    #     )
    #     self.assertEqual(self.solution.maxSlidingWindow([1], 1), [1])

    def test_maxSlidingWindow_additional(self):
        nums = [1, 2, 1, 0, 4, 2, 6]
        k = 3
        expected = [2, 2, 4, 4, 6]
        self.assertEqual(
            self.solution.maxSlidingWindow(nums, k),
            expected,
            "Failed for input: nums=[1,2,1,0,4,2,6], k=3",
        )

    def test_maxSlidingWindow_edge_case(self):
        nums = [1, -1]
        k = 1
        expected = [1, -1]
        self.assertEqual(
            self.solution.maxSlidingWindow(nums, k),
            expected,
            "Failed for input: nums=[1, -1], k=1",
        )

    def test_maxSlidingWindow_additional_case(self):
        nums = [1, 3, 1, 2, 0, 5]
        k = 3
        expected = [3, 3, 2, 5]
        self.assertEqual(
            self.solution.maxSlidingWindow(nums, k),
            expected,
            "Failed for input: nums=[1,3,1,2,0,5], k=3",
        )


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return None

if __name__ == "__main__":
    unittest.main()
