package main

import (
	"fmt"
	"testing"
)

func strStr(haystack string, needle string) int {
	r := 0
	var first int
	for i := 0; i < len(haystack); i += 1 {
		if r > 3 {
			fmt.Printf("")
		}
		if haystack[i] == needle[r] {
			r += 1
		} else {
			i = first
			r = 0
			first = i + 1
		}
		if r == len(needle) {
			return first
		}
	}
	return -1
}

func TestStrStr(t *testing.T) {
	testCases := []struct {
		haystack string
		needle   string
		expected int
	}{
		// {"sadbutsad", "sad", 0},
		// {"leetcode", "leeto", -1},
		{"mississippi", "issip", 4},
	}

	for _, tc := range testCases {
		actual := strStr(tc.haystack, tc.needle)
		if actual != tc.expected {
			t.Errorf("strStr(%q, %q) = %d, expected %d", tc.haystack, tc.needle, actual, tc.expected)
		}
	}
}
