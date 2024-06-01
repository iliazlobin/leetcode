import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestConsecutive(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        self.assertEqual(self.solution.longestConsecutive(nums), 9)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            numSet.add(n)
        longest = 0
        for n in nums:
            if n - 1 not in numSet:
                c = n
                while True:
                    if c in numSet:
                        c += 1
                    else:
                        longest = max(longest, c - n)
                        break
        return longest


if __name__ == "__main__":
    unittest.main()
