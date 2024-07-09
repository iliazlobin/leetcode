package main

import (
	"testing"
)

func majorityElement(nums []int) int {
	count := 0
	res := 0
	for _, n := range nums {
		if count > 0 {
			if res == n {
				count += 1
			} else {
				count -= 1
			}
		} else {
			count += 1
			res = n
		}
	}
	return res
}

func TestMajorityElement(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{[]int{3, 2, 3}, 3},
		{[]int{2, 2, 1, 1, 1, 2, 2}, 2},
	}

	for _, tc := range testCases {
		actual := majorityElement(tc.nums)
		if actual != tc.expected {
			t.Errorf("majorityElement(%v) = %d, expected %d", tc.nums, actual, tc.expected)
		}
	}
}
