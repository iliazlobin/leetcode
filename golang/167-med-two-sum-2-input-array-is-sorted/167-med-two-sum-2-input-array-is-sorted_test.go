package main

import (
	"reflect"
	"testing"
)

func twoSum(numbers []int, target int) []int {
	right := len(numbers) - 1
	for left := 0; left < right; {
		total := numbers[left] + numbers[right]
		if total == target {
			return []int{left + 1, right + 1}
		} else if total < target {
			left++
		} else {
			right--
		}
	}
	return nil
}

func TestTwoSum(t *testing.T) {
	testCases := []struct {
		numbers  []int
		target   int
		expected []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{1, 2}},
		{[]int{2, 3, 4}, 6, []int{1, 3}},
		{[]int{-1, 0}, -1, []int{1, 2}},
	}

	for _, tc := range testCases {
		actual := twoSum(tc.numbers, tc.target)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("twoSum(%v, %d) = %v, expected %v", tc.numbers, tc.target, actual, tc.expected)
		}
	}
}
