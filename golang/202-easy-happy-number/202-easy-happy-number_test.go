package main

import (
	"strconv"
	"testing"
)

func isHappy(n int) bool {
	hMap := make(map[int]bool)
	cur := n
	for {
		new := 0
		for _, c := range strconv.Itoa(cur) {
			new += int(c-'0') * int(c-'0')
		}
		if new == 1 {
			break
		}
		if _, ok := hMap[new]; ok {
			return false
		}
		hMap[new] = true
		cur = new
	}
	return true
}

func TestIsHappy(t *testing.T) {
	testCases := []struct {
		input    int
		expected bool
	}{
		{19, true},
		{2, false},
	}

	for _, tc := range testCases {
		actual := isHappy(tc.input)
		if actual != tc.expected {
			t.Errorf("isHappy(%d) = %v, expected %v", tc.input, actual, tc.expected)
		}
	}
}
