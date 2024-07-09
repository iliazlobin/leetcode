package main

import (
	"testing"
)

func isIsomorphic(s string, t string) bool {
	sMap := make(map[rune]rune)
	for i, c := range s {
		if m, ok := sMap[c]; ok {
			if m != rune(t[i]) {
				return false
			}
		}
		sMap[c] = rune(t[i])
	}
	tMap := make(map[rune]rune)
	for i, c := range t {
		if m, ok := tMap[c]; ok {
			if m != rune(s[i]) {
				return false
			}
		}
		tMap[c] = rune(s[i])
	}
	return true
}

func TestIsIsomorphic(t *testing.T) {
	testCases := []struct {
		s        string
		t        string
		expected bool
	}{
		{"eeg", "aad", true},
		{"foo", "bar", false},
		{"paper", "title", true},
		{"badc", "baba", false},
	}

	for _, tc := range testCases {
		actual := isIsomorphic(tc.s, tc.t)
		if actual != tc.expected {
			t.Errorf("isIsomorphic(%q, %q) = %v, expected %v", tc.s, tc.t, actual, tc.expected)
		}
	}
}
