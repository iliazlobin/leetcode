package main

import (
	"testing"
	"unicode"
)

func isAlphaNumeric(c rune) bool {
	return unicode.IsNumber(c) || unicode.IsLetter(c)
}

func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		if !isAlphaNumeric(rune(s[l])) {
			l++
		} else if !isAlphaNumeric(rune(s[r])) {
			r--
		} else {
			if unicode.ToLower(rune(s[l])) != unicode.ToLower(rune(s[r])) {
				return false
			}
			l++
			r--
		}
	}
	return true
}

func isPalindrome2(s string) bool {
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
