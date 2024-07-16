package main

import (
	"testing"
)

func searchInsert(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		m := int((l + r) / 2)
		if nums[m] == target {
			return m
		} else if nums[m] > target {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l
}

func TestSearchInsert(t *testing.T) {
	testCases := []struct {
		nums     []int
		target   int
		expected int
	}{
		{nums: []int{1, 3, 5, 6}, target: 4, expected: 2},
		{nums: []int{1, 3, 5, 6}, target: 5, expected: 2},
		{nums: []int{1, 3, 5, 6}, target: 2, expected: 1},
		{nums: []int{1, 3, 5, 6}, target: 7, expected: 4},
	}

	for _, tc := range testCases {
		actual := searchInsert(tc.nums, tc.target)
		if actual != tc.expected {
			t.Errorf("searchInsert(%v, %d) = %v, expected %v", tc.nums, tc.target, actual, tc.expected)
		}
	}
}
