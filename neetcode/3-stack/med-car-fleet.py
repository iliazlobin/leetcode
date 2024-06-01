import enum
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = NeetCodeSolution()

    def test_carFleet(self):
        # target = 10
        # position = [1, 4]
        # speed = [3, 2]
        # result = self.solution.carFleet(target, position, speed)
        # self.assertEqual(result, 1)

        # target = 10
        # position = [4, 1, 0, 7]
        # speed = [2, 2, 1, 1]
        # result = self.solution.carFleet(target, position, speed)
        # self.assertEqual(result, 3)

        # target = 10
        # position = [4, 1, 0, 7]
        # speed = [2, 2, 1, 1]
        # result = self.solution.carFleet(target, position, speed)
        # self.assertEqual(result, 3)

        # target = 100
        # position = [0, 2, 4]
        # speed = [4, 2, 1]
        # result = self.solution.carFleet(target, position, speed)
        # self.assertEqual(result, 1)

        # target = 10
        # position = [8, 3, 7, 4, 6, 5]
        # speed = [4, 4, 4, 4, 4, 4]
        # result = self.solution.carFleet(target, position, speed)
        # self.assertEqual(result, 6)

        target = 31
        position = [5, 26, 18, 25, 29, 21, 22, 12, 19, 6]
        speed = [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]
        result = self.solution.carFleet(target, position, speed)
        self.assertEqual(result, 6)


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(speed)
        track_position = [0] * l
        track_fleet = {}

        for pi, p in enumerate(position):
            track_position[pi] = p

        # tracking who finishes
        fleet_map = {}

        step = 0

        while True:
            step += 1

            # calc new track position
            new_track_position = [0] * l
            for pi, p in enumerate(track_position):
                new_track_position[pi] = track_position[pi] + speed[pi]

            calc_track_position = [0] * l
            for pi, p in enumerate(new_track_position):
                is_overtaken = False
                for ni, n in enumerate(new_track_position):
                    if pi == ni:
                        continue
                    if track_position[pi] <= track_position[ni] and p > n:
                        is_overtaken = True
                        if calc_track_position[pi] == 0 or calc_track_position[pi] > n:
                            calc_track_position[pi] = n
                if not is_overtaken:
                    calc_track_position[pi] = new_track_position[pi]

            track_position = calc_track_position

            # check if all finish
            all_finish = True
            for pi, p in enumerate(track_position):
                if p >= target:
                    if pi not in fleet_map:
                        fleet_map[pi] = f"{step}/{p}"
                if p < target:
                    all_finish = False

            unique_steps = set()
            if all_finish:
                for k, v in fleet_map.items():
                    unique_steps.add(v)

                return len(unique_steps)


# calculate the number of steps (time) requires to reach the destination
class NeetCodeSolution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


if __name__ == "__main__":
    unittest.main()
