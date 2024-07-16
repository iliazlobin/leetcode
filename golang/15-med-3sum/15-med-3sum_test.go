package main

import (
	"reflect"
	"sort"
	"testing"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)

	res := [][]int{}
	// []int{-4, -1, -1, 0, 1, 2}
	// for i, n := range nums {
	for i := 0; i < len(nums); i += 1 {
		n := nums[i]
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		if i == len(nums)-2 {
			break
		}

		l, r := i+1, len(nums)-1
		for l < r {
			sum := n + nums[l] + nums[r]
			if sum < 0 {
				l += 1
			} else if sum > 0 {
				r -= 1
			} else {
				res = append(res, []int{n, nums[l], nums[r]})
				for l+1 < r && nums[l+1] == nums[l] {
					l += 1
				}
				l += 1
			}
		}
	}

	return res
}

func TestThreeSum(t *testing.T) {
	testCases := []struct {
		nums     []int
		expected [][]int
	}{
		{
			nums:     []int{-1, 0, 1, 2, -1, -4},
			expected: [][]int{{-1, -1, 2}, {-1, 0, 1}},
		},
		{
			nums:     []int{0, 1, 1},
			expected: [][]int{},
		},
		{
			nums:     []int{0, 0, 0},
			expected: [][]int{{0, 0, 0}},
		},
	}

	for _, tc := range testCases {
		actual := threeSum(tc.nums)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("threeSum(%v) = %v, expected %v", tc.nums, actual, tc.expected)
		}
	}
}
