import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_restoreIpAddresses_example1(self):
    #     s = "25525511135"
    #     expected = ["255.255.11.135", "255.255.111.35"]
    #     result = self.solution.restoreIpAddresses(s)
    #     self.assertEqual(
    #         sorted(expected),
    #         sorted(result),
    #         f"Failed on Example 1 with {result} != {expected}",
    #     )

    # def test_restoreIpAddresses_example2(self):
    # s = "0000"
    # expected = ["0.0.0.0"]
    # result = self.solution.restoreIpAddresses(s)
    # self.assertEqual(
    #     expected, result, f"Failed on Example 2 with {result} != {expected}"
    # )

    def test_restoreIpAddresses_example3(self):
        s = "101023"
        expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
        result = self.solution.restoreIpAddresses(s)
        self.assertEqual(
            sorted(expected),
            sorted(result),
            f"Failed on Example 3 with {result} != {expected}",
        )


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(i, sub):
            if i == len(s):
                if len(sub) == 4:
                    res.append(sub.copy())
                return
            if len(sub) == 4:
                return

            for j in range(i + 1, min(i + 4, len(s) + 1)):
                ss = s[i:j]
                if len(ss) > 1 and ss[0] == "0":
                    break
                n = int(ss)
                if n > 255:
                    break
                dfs(j, sub + [ss])

        dfs(0, [])
        for i in range(len(res)):
            res[i] = ".".join(res[i])
        return res


if __name__ == "__main__":
    unittest.main()
