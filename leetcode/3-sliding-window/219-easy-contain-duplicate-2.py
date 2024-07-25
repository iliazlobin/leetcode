import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_containsNearbyDuplicate_example1(self):
        nums = [1, 2, 3, 1]
        k = 3
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertTrue(result)

    def test_containsNearbyDuplicate_example2(self):
        nums = [1, 0, 1, 1]
        k = 1
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertTrue(result)

    def test_containsNearbyDuplicate_example3(self):
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertFalse(result)


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for r in range(len(nums)):
            if nums[r] in indices:
                return True
            indices[nums[r]] = r
            if r - k >= 0:
                del indices[nums[r - k]]
        return False


if __name__ == "__main__":
    unittest.main()
