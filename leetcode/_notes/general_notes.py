import unittest
from collections import defaultdict
from typing import List, Optional

match term:
    case pattern-1:
            action-1
    case pattern-2:
            action-2
operatorsFuncs = {
    "-": lambda a, b: int(a) - int(b),
    "+": lambda a, b: int(a) + int(b),
    "*": lambda a, b: int(a) * int(b),
    "/": lambda a, b: int(int(a) / int(b)),
}

text = "10#neetcode"
textInd = text.find("#")  # 2
textLen = text[textInd:]

nums = [1, 2, 3]
freq = [[] for _ in range(len(nums) + 1)]
prefix = [1] * len(nums)

rows, cols = defaultdict(set), defaultdict(set)
collect = set()
s = "palindrome"
l, r = 0, len(s)
while l <= r:
    if s[l].isalpha():
        l += 1

position: List[int] = []
speed: List[int] = []
pair = [(p, s) for p, s in zip(position, speed)]
pair.sort(key=lambda pair: pair[0], reverse=True)

nums = [-1,0,2,4,6,8]
target = 4
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] > target:
        r = m - 1
    elif nums[m] < target:
        l = m + 1
    else:
        return m

l, r = 0, len(nums) - 1
while l <= r:
    m: int = (l + r) // 2
    if target == nums[m]:
        return m
    if nums[l] <= nums[m]:
        if target > nums[m] or target < nums[l]:
            l = m + 1
        else:
            r = m - 1
    else:
        if target < nums[m] or target > nums[r]:
            r = m - 1
        else:
            l = m + 1
# return -1

def permute(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [[nums[0]]]

    res = []
    for i in nums:
        n = nums.pop(0)
        perms = self.permute(nums)
        for p in perms:
            p.append(n)
        res.extend(perms)
        nums.append(n)

# largest rectangle area
stack = []
heights: List[int] = []
for i, h in enumerate(iterable=heights):
    start = i
    while stack and stack[-1][1] > h:
        index, height = stack.pop()
        width = i - index
        maxArea = max(maxArea, height * width)
        start = index
    stack.append((start, h))

for i, h in stack:
    width = len(heights) - i
    maxArea = max(maxArea, width * h)

# subarrays mins
arr = [0] + arr
res = [0] * len(arr)
stack = [0]
for i in range(len(arr)):
    while stack and arr[stack[-1]] > arr[i]:
        stack.pop()
    res[i] = res[stack[-1]] + (i - stack[-1]) * arr[i]
    stack.append(i)
# return sum(res) % (10**9 + 7)

# reverse colors
i, l, r = 0, 0, len(nums) - 1
# [2, 0, 2, 1, 1, 0]
while i <= r:
if nums[i] == 0:
    nums[l], nums[i] = nums[i], nums[l]
    l += 1
    i += 1
elif nums[i] == 2:
    nums[i], nums[r] = nums[r], nums[i]
    r -= 1
else:
    i += 1

# string balance
imbalance = 0
for c in s:
    if c == "[":
        imbalance += 1
    elif imbalance > 0:
        imbalance -= 1
# return (imbalance + 1 ) // 2

# hand of straights
minH = list(count.keys())
heapq.heapify(minH)

while minH:
    first = minH[0]

    for c in range(first, first + groupSize):
        if c not in count:
            return False
        count[c] -= 1
        if count[c] == 0:
            heapq.heappop(minH)
