import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_asteroidCollision_example1(self):
        self.assertEqual(self.solution.asteroidCollision([5, 10, -5]), [5, 10])

    def test_asteroidCollision_example2(self):
        self.assertEqual(self.solution.asteroidCollision([8, -8]), [])

    def test_asteroidCollision_example3(self):
        self.assertEqual(self.solution.asteroidCollision([10, 2, -5]), [10])

    def test_asteroidCollision_example4(self):
        self.assertEqual(
            self.solution.asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2]
        )


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            a = asteroids[i]
            skip = False
            while stack and a < 0 and stack[-1] > 0:
                if -1 * a >= stack[-1]:
                    prev = stack.pop()
                    if -1 * a == prev:
                        skip = True
                        break
                else:
                    skip = True
                    break
            if skip:
                continue
            stack.append(a)
        return stack


if __name__ == "__main__":
    unittest.main()
