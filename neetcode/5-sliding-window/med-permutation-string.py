import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_checkInclusion(self):
        s1 = "abc"
        s2 = "lecabee"
        result = self.solution.checkInclusion(s1, s2)
        self.assertTrue(result)

        s1 = "abc"
        s2 = "lecaabee"
        result = self.solution.checkInclusion(s1, s2)
        self.assertFalse(result)

        s1 = "abc"
        s2 = "lecaabee"
        result = self.solution.checkInclusion(s1, s2)
        self.assertFalse(result)

        s1 = "ab"
        s2 = "lecabee"
        result = self.solution.checkInclusion(s1, s2)
        self.assertTrue(result)

        s1 = "ab"
        s2 = "ab"
        result = self.solution.checkInclusion(s1, s2)
        self.assertTrue(result)

        s1 = "sea"
        s2 = "eat"
        result = self.solution.checkInclusion(s1, s2)
        self.assertFalse(result)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s1), len(s2) + 1):
            sub = s2[i - len(s1) : i]

            search = s1
            for c in sub:
                found = False
                for vi, v in enumerate(search):
                    if c == v:
                        if vi == 0:
                            search = search[1:]
                        elif vi == len(search) - 1:
                            search = search[0:vi]
                        else:
                            search = search[0 : vi] + search[vi + 1 :]
                        found = True
                        break
                if not found:
                    break
                if len(search) == 0:
                    return True
        return False


if __name__ == "__main__":
    unittest.main()
