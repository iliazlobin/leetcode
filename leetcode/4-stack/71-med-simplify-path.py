import unittest
from collections import Counter
from typing import List, Literal, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simplifyPath(self):
        # Example 1
        path = "/home/"
        expected = "/home"
        self.assertEqual(
            self.solution.simplifyPath(path), expected, "Failed for Example 1"
        )

        # Example 2
        path = "/home//foo/"
        expected = "/home/foo"
        self.assertEqual(
            self.solution.simplifyPath(path), expected, "Failed for Example 2"
        )

        # Example 3
        path = "/home/user/Documents/../Pictures"
        expected = "/home/user/Pictures"
        self.assertEqual(
            self.solution.simplifyPath(path), expected, "Failed for Example 3"
        )

        # Example 4
        path = "/../"
        expected = "/"
        self.assertEqual(
            self.solution.simplifyPath(path), expected, "Failed for Example 4"
        )

        # Example 5
        path = "/.../a/../b/c/../d/./"
        expected = "/.../b/d"
        self.assertEqual(
            self.solution.simplifyPath(path), expected, "Failed for Example 5"
        )


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        for p in paths:
            if p == "" or p == ".":
                continue
            if p == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(p)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    unittest.main()
