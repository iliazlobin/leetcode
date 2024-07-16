package main

import (
	"strconv"
	"testing"
)

func isHappy(n int) bool {
	hmap := make(map[int]bool)

	for {
		new := 0
		for _, c := range strconv.Itoa(n) {
			v := int(c - '0')
			new += v * v
		}
		if new == 1 {
			return true
		}
		if _, ok := hmap[new]; ok {
			return false
		}
		hmap[new] = true
		n = new
	}
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
