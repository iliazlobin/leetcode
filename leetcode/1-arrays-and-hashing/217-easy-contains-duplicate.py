import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_containsDuplicate(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.containsDuplicate(nums), True)

        nums = [1, 2, 3, 4]
        self.assertEqual(self.solution.containsDuplicate(nums), False)

        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertEqual(self.solution.containsDuplicate(nums), True)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


if __name__ == "__main__":
    unittest.main()
