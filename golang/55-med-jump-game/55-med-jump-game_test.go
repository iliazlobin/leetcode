package main

import (
	"testing"
)

func canJump(nums []int) bool {
	goal := len(nums) - 1
	for i := len(nums) - 2; i >= 0; i -= 1 {
		dist := goal - i
		if nums[i] >= dist {
			goal = i
		}
	}

	return goal == 0
}

func TestCanJump(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected bool
	}{
		{
			nums:     []int{2, 3, 1, 1, 4},
			expected: true,
		},
		{
			nums:     []int{3, 2, 1, 0, 4},
			expected: false,
		},
	}

	for _, tc := range testCases {
		actual := canJump(tc.nums)
		if actual != tc.expected {
			t.Errorf("canJump(%v) = %v, expected %v", tc.nums, actual, tc.expected)
		}
	}
}
