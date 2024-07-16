package main

import (
	"testing"
)

func rotate(nums []int, k int) {
	shift := k % len(nums)

	if shift == len(nums) {
		return
	}

	l, r := 0, len(nums)-1
	for l < r {
		nums[l], nums[r] = nums[r], nums[l]
		l += 1
		r -= 1
	}

	l, r = 0, shift - 1
	for l < r {
		nums[l], nums[r] = nums[r], nums[l]
		l += 1
		r -= 1
	}

	l, r = shift, len(nums)-1
	for l < r {
		nums[l], nums[r] = nums[r], nums[l]
		l += 1
		r -= 1
	}
}

func rotateM(nums []int, k int) {
	shift := len(nums) - (k % len(nums)) // 1

	if shift == len(nums) {
		return
	}

	leftPart := nums[:shift]
	rightPart := nums[shift:]

	for i, n := range append(rightPart, leftPart...) {
		nums[i] = n
	}
}

func TestRotate(t *testing.T) {
	testCases := []struct {
		nums     []int
		k        int
		expected []int
	}{
		{
			nums:     []int{1, 2, 3, 4, 5, 6, 7},
			k:        3,
			expected: []int{5, 6, 7, 1, 2, 3, 4},
		},
		{
			nums:     []int{-1, -100, 3, 99},
			k:        2,
			expected: []int{3, 99, -1, -100},
		},
	}

	for _, tc := range testCases {
		rotate(tc.nums, tc.k) // This modifies tc.nums in-place
		if !equal(tc.nums, tc.expected) {
			t.Errorf("After rotate(%v, %d), got %v, expected %v", tc.nums, tc.k, tc.nums, tc.expected)
		}
	}
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
