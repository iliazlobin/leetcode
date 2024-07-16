package main

import (
	"testing"
)

func strStr(haystack string, needle string) int {
	p := 0
	for i := 0; i < len(haystack); i += 1 {
		c := rune(haystack[i])
		if c != rune(needle[p]) {
			i -= p
			p = 0
		} else {
			p += 1
			if p == len(needle) {
				return i - p + 1
			}
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
