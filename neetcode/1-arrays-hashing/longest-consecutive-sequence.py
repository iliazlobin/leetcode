import unittest
from typing import List, Optional


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longest = 0
        count = 1
        prev = nums[0]
        for i, n in enumerate(iterable=nums):
            if i == 0:
                continue
            if n == prev:
                continue
            if n == prev + 1:
                count += 1
            else:
                if count > longest:
                    longest = count
                count = 1
            prev = n
        if longest == 0:
            longest = count
        if count > longest:
            longest = count
        return longest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_consecutive_sequence(self):
        # nums = [2,20,4,10,3,4,5]
        # result = self.solution.longestConsecutive(nums)
        # self.assertEqual(result, 4)

        # nums = [0,3,2,5,4,6,1,1]
        # result = self.solution.longestConsecutive(nums)
        # self.assertEqual(result, 7)

        nums = [9,1,4,7,3,-1,0,5,8,-1,6]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()
