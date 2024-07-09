package main

import (
	"testing"
)

func canConstruct(ransomNote string, magazine string) bool {
	hMap := make(map[rune]int)
	for _, c := range magazine {
		hMap[c]++
	}
	for _, c := range ransomNote {
		hMap[c]--
		if hMap[c] < 0 {
			return false
		}
	}
	return true
}

func TestCanConstruct(t *testing.T) {
	testCases := []struct {
		ransomNote string
		magazine   string
		expected   bool
	}{
		{"a", "b", false},
		{"aa", "ab", false},
		{"aa", "aab", true},
	}

	for _, tc := range testCases {
		actual := canConstruct(tc.ransomNote, tc.magazine)
		if actual != tc.expected {
			t.Errorf("canConstruct(%q, %q) = %v, expected %v", tc.ransomNote, tc.magazine, actual, tc.expected)
		}
	}
}
