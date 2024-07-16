package main

import (
	"testing"
)

func jump(nums []int) int {
	l, r := 0, 0
	jumps := 0

	for r < len(nums)-1 {
		furthest := 0
		jumps += 1
		for i := l; i < r+1; i += 1 {
			if i+nums[i] > furthest {
				furthest = i + nums[i]
			}
			if i == r {
				l = r + 1
				r = furthest
				break
			}
		}
	}

	return jumps
}

func TestJump(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{
			nums:     []int{2, 3, 1, 1, 4},
			expected: 2,
		},
		{
			nums:     []int{2, 3, 0, 1, 4},
			expected: 2,
		},
	}

	for _, tc := range testCases {
		actual := jump(tc.nums)
		if actual != tc.expected {
			t.Errorf("jump(%v) = %d, expected %d", tc.nums, actual, tc.expected)
		}
	}
}
