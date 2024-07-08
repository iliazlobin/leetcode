package main

import (
	"reflect"
	"testing"
)

func plusOne(digits []int) []int {
	n := 0
	carry := 0
	for i := len(digits) - 1; i >= 0; i-- {
		if i == len(digits)-1 {
			n = digits[i] + 1 + carry
		} else if carry > 0 {
			n = digits[i] + carry
		} else {
			break
		}
		if n >= 10 {
			carry = 1
			digits[i] = n % 10
		} else {
			carry = 0
			digits[i] = n
		}
	}
	if carry > 0 {
		digits = append([]int{1}, digits...)
	}
	return digits
}

// simplified version, more efficient
func plusOneC(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	return append([]int{1}, digits...)
}

func TestPlusOne(t *testing.T) {
	testCases := []struct {
		input    []int
		expected []int
	}{
		{[]int{1, 2, 3}, []int{1, 2, 4}},
		{[]int{4, 3, 2, 1}, []int{4, 3, 2, 2}},
		{[]int{9}, []int{1, 0}},
	}

	for _, tc := range testCases {
		actual := plusOne(tc.input)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("plusOne(%v) = %v, expected %v", tc.input, actual, tc.expected)
		}
	}
}
