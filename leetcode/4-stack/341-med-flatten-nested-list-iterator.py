import unittest
from collections import Counter
from typing import List, Optional


class TestNestedIterator(unittest.TestCase):
    def test_flatten_nested_list_example1(self):
        nestedList = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
        iterator = NestedIterator(nestedList)
        res = []
        while iterator.hasNext():
            res.append(iterator.next())
        self.assertEqual(res, [1, 1, 2, 1, 1], "Expected output does not match the actual output.")

    def test_flatten_nested_list_example2(self):
        nestedList = [NestedInteger(1), NestedInteger([NestedInteger(4), NestedInteger([NestedInteger(6)])])]
        iterator = NestedIterator(nestedList)
        res = []
        while iterator.hasNext():
            res.append(iterator.next())
        self.assertEqual(res, [1, 4, 6], "Expected output does not match the actual output.")

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._list = []
            self._integer = None
        elif isinstance(value, int):
            self._integer = value
            self._list = None
        else:  # Assume value is a list of NestedInteger
            self._list = value
            self._integer = None

    def isInteger(self):
        return self._integer is not None

    def add(self, elem):
        if self._list is None:
            self._list = []
        self._list.append(elem)

    def setInteger(self, value):
        self._integer = value

    def getInteger(self):
        return self._integer

    def getList(self):
        return self._list

class NestedIterator:
    stack = []

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.dfs(nestedList)

    def dfs(self, nestedList: NestedInteger):
        if nestedList.isInteger():
            self.stack.append(nestedList.getInteger())
        else:
            self.dfs(nestedList.getList())
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    unittest.main()
