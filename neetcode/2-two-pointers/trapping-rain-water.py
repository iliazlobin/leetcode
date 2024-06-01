import unittest
from typing import List, Optional


class Solution:
    def trap(self, height: List[int]) -> int:
        maxs = []
        for i, cur in enumerate(height):
            if i == 0:
                if i == len(height) - 1:
                    continue
                next = height[i + 1]
                if cur >= next:
                    maxs.append({"index": i, "height": cur})
                continue
            elif i == len(height) - 1:
                prev = height[i - 1]
                if cur >= prev:
                    maxs.append({"index": i, "height": cur})
                continue
            prev = height[i - 1]
            next = height[i + 1]
            if cur >= prev and cur >= next:
                maxs.append({"index": i, "height": cur})
        print()
        sorted_maxs = sorted(maxs, key=lambda x: x["index"], reverse=False)
        total_capacity = 0

        processed_index = 0
        for i, item in enumerate(sorted_maxs):
            if not i < len(sorted_maxs) - 1:
                break
            if i < processed_index:
                continue
            this_index = item["index"]
            this_height = item["height"]

            next_index = sorted_maxs[i+1]["index"]
            next_height = sorted_maxs[i+1]["height"]

            # determine the next max on the left
            for ii, next_item in enumerate(sorted_maxs):
                if ii <= i:
                    continue
                ind = next_item["index"]
                hgt = next_item["height"]
                if this_height > next_height and next_height < hgt:
                    processed_index = ii
                    next_index = ind
                    next_height = hgt

            # calc capacity
            min_height = (
                this_height if this_height <= next_height else next_height
            )
            this_capacity = 0
            for i in range(this_index + 1, next_index):
                current_height = height[i]
                capacity = min_height - current_height if current_height < min_height else 0
                this_capacity += capacity

            total_capacity += this_capacity

        return total_capacity

class DraftSolution:
    def trap(self, height: List[int]) -> int:
        maxs = []
        for i, cur in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            prev = height[i - 1]
            next = height[i + 1]
            if cur >= prev and cur >= next:
                maxs.append({"index": i, "height": cur})
        print()
        sorted_maxs = sorted(maxs, key=lambda x: x["index"], reverse=False)
        print()
        total_capacity = 0

        next_max_index = 0
        next_max_height = 0

        for i, item in enumerate(sorted_maxs):
            # if i < next_max_index:
            #     continue
            if not i < len(sorted_maxs) - 1:
                break
            this_index = item["index"]
            this_height = item["height"]

            # # determine the next max
            # for ii, next_item in enumerate(sorted_maxs):
            #     if ii <= i:
            #         continue
            #     next_index = next_item["index"]
            #     next_height = next_item["height"]
            #     if next_max_height < next_height:
            #         next_max_index = next_index
            #         next_max_height = next_height

            next_index = sorted_maxs[i+1]["index"]
            next_height = sorted_maxs[i+1]["height"]

            # calc capacity
            min_height = (
                this_height if this_height <= next_height else next_height
            )
            this_capacity = 0
            for i in range(this_index + 1, next_index):
                current_height = height[i]
                capacity = min_height - current_height
                this_capacity += capacity
            total_capacity += this_capacity

        return total_capacity

class NeetCodeSolution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_area(self):
        heights = [0]
        result = self.solution.trap(heights)
        self.assertEqual(result, 0)

        heights = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
        result = self.solution.trap(heights)
        self.assertEqual(result, 9)

        heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        result = self.solution.trap(heights)
        self.assertEqual(result, 6)

        heights = [4,2,0,3,2,5]
        result = self.solution.trap(heights)
        self.assertEqual(result, 9)

        heights = [5,4,1,2]
        result = self.solution.trap(heights)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
