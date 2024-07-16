package main

import (
	"math"
	"testing"
)

func minSubArrayLen(target int, nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	res := math.MaxInt
	l, r := 0, 0
	sum := nums[0]
	// [2,3,1,2,4,3]
	for {
		if sum >= target {
			length := r - l + 1

			if length < res {
				res = length
				if res == 1 {
					return res
				}
			}

			sum -= nums[l]
			l += 1
		} else {
			r += 1
			if r == len(nums) {
				break
			}
			sum += nums[r]
		}
	}

	if res == math.MaxInt {
		res = 0
	}
	return res
}

func TestMinSubArrayLen(t *testing.T) {
	testCases := []struct {
		target   int
		nums     []int
		expected int
	}{
		{
			target:   7,
			nums:     []int{2, 3, 1, 2, 4, 3},
			expected: 2,
		},
		{
			target:   4,
			nums:     []int{1, 4, 4},
			expected: 1,
		},
		{
			target:   11,
			nums:     []int{1, 1, 1, 1, 1, 1, 1, 1},
			expected: 0,
		},
	}

	for _, tc := range testCases {
		actual := minSubArrayLen(tc.target, tc.nums)
		if actual != tc.expected {
			t.Errorf("minSubArrayLen(%d, %v) = %d, expected %d", tc.target, tc.nums, actual, tc.expected)
		}
	}
}
