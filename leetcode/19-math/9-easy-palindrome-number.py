import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome(self):
        self.assertTrue(self.solution.isPalindrome(121), "121 is a palindrome")
        self.assertFalse(self.solution.isPalindrome(-121), "-121 is not a palindrome")
        self.assertFalse(self.solution.isPalindrome(10), "10 is not a palindrome")


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        cur = x
        while cur > 0:
            reversed = (cur % 10) + reversed * 10
            cur = cur // 10
        return reversed == x


if __name__ == "__main__":
    unittest.main()
