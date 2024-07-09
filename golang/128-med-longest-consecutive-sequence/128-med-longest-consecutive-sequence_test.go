package main

import (
	"sort"
	"testing"
)

func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	sort.Ints(nums)
	maxSeq := 1
	curSeq := 1
	for i := range nums {
		if i > 0 && nums[i-1]+1 == nums[i] {
			curSeq += 1
			if curSeq > maxSeq {
				maxSeq = curSeq
			}
		} else if i > 0 && nums[i-1]+1 < nums[i] {
			curSeq = 1
		}
	}
	return maxSeq
}

func TestLongestConsecutive(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{[]int{100, 4, 200, 1, 3, 2}, 4},
		{[]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}, 9},
		{[]int{1, 2, 0, 1}, 3},
	}

	for _, tc := range testCases {
		actual := longestConsecutive(tc.nums)
		if actual != tc.expected {
			t.Errorf("longestConsecutive(%v) = %d, expected %d", tc.nums, actual, tc.expected)
		}
	}
}
