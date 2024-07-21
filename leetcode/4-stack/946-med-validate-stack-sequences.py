import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_validateStackSequences_example1(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 5, 3, 2, 1]
        self.assertTrue(self.solution.validateStackSequences(pushed, popped))

    def test_validateStackSequences_example2(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 3, 5, 1, 2]
        self.assertFalse(self.solution.validateStackSequences(pushed, popped))


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        while True:
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            if i == len(pushed):
                break
            stack.append(pushed[i])
            i += 1
        return len(stack) == 0


if __name__ == "__main__":
    unittest.main()
