import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_MinStack_example1(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3, "getMin should return -3")
        minStack.pop()
        self.assertEqual(minStack.top(), 0, "top should return 0")
        self.assertEqual(minStack.getMin(), -2, "getMin should return -2")

    def test_MinStack_example2(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(2)
        self.assertEqual(minStack.top(), 2, "top should return 2")
        self.assertEqual(minStack.getMin(), 1, "getMin should return 1")
        minStack.pop()
        self.assertEqual(minStack.getMin(), 1, "getMin should return 1 after pop")


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return -1


if __name__ == "__main__":
    unittest.main()
