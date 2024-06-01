from multiprocessing import connection
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_threeSum(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = self.solution.threeSum(nums)
        for triplet in result:
            self.assertIn(sorted(triplet), [sorted(x) for x in expected])

        nums = [0, 1, 1]
        expected = []
        self.assertEqual(self.solution.threeSum(nums), expected)

        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.threeSum(nums)
        for triplet in result:
            self.assertIn(sorted(triplet), [sorted(x) for x in expected])

        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = self.solution.threeSum(nums)
        self.assertTrue(
            all(sorted(triplet) in [sorted(x) for x in expected] for triplet in result)
        )
        self.assertEqual(len(result), len(expected))

        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.threeSum(nums)
        self.assertEqual(
            sorted([sorted(x) for x in result]), sorted([sorted(x) for x in expected])
        )


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # because there won't be any opportunity to decrease the total with the rest of the numbers after 0
                break
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r = r - 1
                elif s < 0:
                    l = l + 1
                else:
                    # if nums[l] != nums[r]:
                    res.append([a, nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                    while nums[l] == nums[l - 1] and l < r:
                        l = l + 1

        return res


class NSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


if __name__ == "__main__":
    unittest.main()
