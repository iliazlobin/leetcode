import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = NeetCodeSolution()
        self.solution = Solution()

    def test_maxSlidingWindow(self):
        # nums = [1, 2, 1, 0, 4, 2, 6]
        # k = 3
        # result = self.solution.maxSlidingWindow(nums, k)
        # self.assertEqual(result, [2, 2, 4, 4, 6])

        nums = [1, 3, 1, 0, 2, 2, 6]
        k = 3
        result = self.solution.maxSlidingWindow(nums, k)
        self.assertEqual(result, [2, 2, 4, 4, 6])


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or k > len(nums):
            return []
        maxs = []
        for r in range(k - 1, len(nums)):
            l = r - k + 1
            sub = nums[l : r + 1]
            max = sub[0]
            for si, s in enumerate(sub):
                if si == 0:
                    continue
                if s > max:
                    max = s
            maxs.append(max)
        return maxs


from collections import deque


class NeetCodeSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output


if __name__ == "__main__":
    unittest.main()
