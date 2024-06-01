import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.minStack = MinStack()

    def test_MinStack(self):
        self.minStack.push(1)
        self.minStack.push(2)
        self.minStack.push(0)
        self.assertEqual(self.minStack.getMin(), 0)
        self.minStack.pop()
        self.assertEqual(self.minStack.top(), 2)
        self.assertEqual(self.minStack.getMin(), 1)

        # ... other test cases ...


class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        return self.data.pop() if self.data else None

    def top(self) -> int:
        if not self.data:
            return 0
        return self.data[-1]

    def getMin(self) -> int:
        if not self.data:
            return None
        min_el = None
        for el in self.data:
            num_el = int(el)
            if min_el is None and isinstance(el, int):
                min_el = el
                continue
            if num_el < min_el:
                min_el = num_el

        return min_el


# Official solution uses 2 stacks to comply with O(1) requirements
# their getMin() function works considerably faster without needing to traverse the list all over again
class NeetCodeMinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == "__main__":
    unittest.main()
