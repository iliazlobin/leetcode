import unittest
from typing import List, Optional


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # processed = s.replace(" ", "").replace("?", "").lower()
        processed = ''.join(c for c in s if c.isalpha() or c.isnumeric()).lower()
        l = len(processed)
        is_palindrome = True
        for i, c in enumerate(processed):
            if i >= l / 2:
                break
            if c != processed[l - i - 1]:
                is_palindrome = False
                break
        return is_palindrome


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_palindrome(self):
        s = "Was it a car or a cat I saw?"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, True)

        s = "tab a cat"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, False)

        s = "Madam, in Eden, I'm Adam"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, True)

        s = "0P"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
