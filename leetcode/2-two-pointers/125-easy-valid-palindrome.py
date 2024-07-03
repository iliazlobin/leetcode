import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome(self):
        s = "A man, a plan, a canal: Panama"
        self.assertEqual(self.solution.isPalindrome(s), True)

        s = "race a car"
        self.assertEqual(self.solution.isPalindrome(s), False)

        s = " "
        self.assertEqual(self.solution.isPalindrome(s), True)

        s = "0P"
        self.assertEqual(self.solution.isPalindrome(s), False)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True

    # def alphaNum(self, c):
    #     return (
    #         ord("A") <= ord(c) <= ord("Z")
    #         or ord("a") <= ord(c) <= ord("z")
    #         or ord("0") <= ord(c) <= ord("9")
    #     )


if __name__ == "__main__":
    unittest.main()
