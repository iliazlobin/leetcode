package main

import (
	"reflect"
	"testing"
)

func permute(nums []int) [][]int {
	if len(nums) == 1 {
		return [][]int{{nums[0]}}
	}

	res := [][]int{}
	for range nums {
		n := nums[0]
		nums = nums[1:]

		perms := permute(nums)
		for i := range perms {
			perms[i] = append(perms[i], n)
		}
		res = append(res, perms...)

		nums = append(nums, n)
	}

	return res
}

func TestPermute(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected [][]int
	}{
		{
			nums: []int{1, 2, 3},
			expected: [][]int{
				{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1},
			},
		},
		{
			nums:     []int{0, 1},
			expected: [][]int{{0, 1}, {1, 0}},
		},
		{
			nums:     []int{1},
			expected: [][]int{{1}},
		},
	}

	for _, tc := range testCases {
		actual := permute(tc.nums)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("permute(%v) = %v, expected %v", tc.nums, actual, tc.expected)
		}
	}
}
