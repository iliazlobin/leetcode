import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_productExceptSelf(self):
        nums = [1, 2, 4, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), [48, 24, 12, 8])

        nums = [-1, 0, 1, 2, 3]
        self.assertEqual(self.solution.productExceptSelf(nums), [0, -6, 0, 0, 0])


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        res = []
        for i in range(len(nums)):
            prefixValue = prefix[i - 1] if i - 1 >= 0 else 1
            postfixValue = postfix[i + 1] if i + 1 <= len(nums) - 1 else 1
            res.append(prefixValue * postfixValue)

        return res


if __name__ == "__main__":
    unittest.main()
