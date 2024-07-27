import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numRescueBoats_example1(self):
        people = [1, 2]
        limit = 3
        expected_output = 1
        self.assertEqual(self.solution.numRescueBoats(people, limit), expected_output)

    def test_numRescueBoats_example2(self):
        people = [3, 2, 2, 1]
        limit = 3
        expected_output = 3
        self.assertEqual(self.solution.numRescueBoats(people, limit), expected_output)

    def test_numRescueBoats_example3(self):
        people = [3, 5, 3, 4]
        limit = 5
        expected_output = 4
        self.assertEqual(self.solution.numRescueBoats(people, limit), expected_output)

    def test_numRescueBoats_custom(self):
        people = [5, 1, 4, 2]
        limit = 6
        expected_output = 2
        self.assertEqual(self.solution.numRescueBoats(people, limit), expected_output)


# [1, 2, 4, 5]
# [3, 3, 4, 5] limit=5
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        while r >= l:
            if r != l and people[r] + people[l] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1
            res += 1
        return res


if __name__ == "__main__":
    unittest.main()
