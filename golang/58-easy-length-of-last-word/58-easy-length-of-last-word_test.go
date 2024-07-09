package main

import (
	"testing"
)

func lengthOfLastWord(s string) int {
	length := 0
	lastLength := 0
	for _, c := range s {
		if c == ' ' {
			if length != 0 {
				lastLength = length
			}
			length = 0
		} else {
			length += 1
		}
	}
	if length != 0 {
		lastLength = length
	}
	return lastLength
}

func TestLengthOfLastWord(t *testing.T) {
	testCases := []struct {
		input    string
		expected int
	}{
		{"Hello World", 5},
		{"   fly me   to   the moon  ", 4},
		{"luffy is still joyboy", 6},
	}

	for _, tc := range testCases {
		actual := lengthOfLastWord(tc.input)
		if actual != tc.expected {
			t.Errorf("lengthOfLastWord(%q) = %d, expected %d", tc.input, actual, tc.expected)
		}
	}
}
