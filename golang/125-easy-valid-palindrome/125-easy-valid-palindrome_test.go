package main

import (
	"testing"
	"unicode"
)

func isPalindrome(s string) bool {
	r := len(s) - 1
	for l := 0; l < r; l += 1 {
		lc := unicode.ToLower(rune(s[l]))
		if !(unicode.IsLetter(lc) || unicode.IsNumber(lc)) {
			continue
		}
		var rc rune
		found := false
		for r > l {
			rc = unicode.ToLower(rune(s[r]))
			r -= 1
			if unicode.IsLetter(rc) || unicode.IsNumber(rc) {
				found = true
				break
			}
		}
		if found && lc != rc {
			return false
		}
	}
	return true
}

func TestIsPalindrome(t *testing.T) {
	testCases := []struct {
		input    string
		expected bool
	}{
		{"A man, a plan, a canal: Panama", true},
		{"race a car", false},
		{" ", true},
		{"ab", false},
		{"a.", true},
	}

	for _, tc := range testCases {
		actual := isPalindrome(tc.input)
		if actual != tc.expected {
			t.Errorf("isPalindrome(%q) = %v, expected %v", tc.input, actual, tc.expected)
		}
	}
}
