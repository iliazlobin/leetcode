package main

import (
	"testing"
)

func searchInsert(nums []int, target int) int {
	r := len(nums) - 1
	l := 0

	for l <= r {
		mid := int((r + l) / 2)
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid - 1
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
		// {nums: []int{1, 3, 5, 6}, target: 5, expected: 2},
		// {nums: []int{1, 3, 5, 6}, target: 2, expected: 1},
		{nums: []int{1, 3, 5, 6}, target: 7, expected: 4},
	}

	for _, tc := range testCases {
		actual := searchInsert(tc.nums, tc.target)
		if actual != tc.expected {
			t.Errorf("searchInsert(%v, %d) = %v, expected %v", tc.nums, tc.target, actual, tc.expected)
		}
	}
}
