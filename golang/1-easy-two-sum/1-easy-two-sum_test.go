package main

import (
	"reflect"
	"testing"
)

func twoSum(nums []int, target int) []int {
	diffMap := make(map[int]int)
	for i, n := range nums {
		if diffInd, ok := diffMap[n]; ok {
			return []int{diffInd, i}
		}
		diff := target - n
		diffMap[diff] = i
	}
	return nil
}

func TestTwoSum(t *testing.T) {
	testCases := []struct {
		nums     []int
		target   int
		expected []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}

	for _, tc := range testCases {
		actual := twoSum(tc.nums, tc.target)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("twoSum(%v, %d) = %v, expected %v", tc.nums, tc.target, actual, tc.expected)
		}
	}
}
