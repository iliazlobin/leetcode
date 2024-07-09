package main

import (
	"testing"
)

func romanToInt(s string) int {
	numerals := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	composedNumerals := map[string]int{
		"IV": 4,
		"IX": 9,
		"XL": 40,
		"XC": 90,
		"CD": 400,
		"CM": 900,
	}
	res := 0
	for i := 0; i < len(s); i++ {
		if i+1 < len(s) {
			cc := s[i : i+2]
			if n, ok := composedNumerals[cc]; ok {
				res += n
				i += 1
				continue
			}
		}
		c := string(s[i])
		if n, ok := numerals[c]; ok {
			res += n
		}
	}
	return res
}

func TestRomanToInt(t *testing.T) {
	testCases := []struct {
		input    string
		expected int
	}{
		{"III", 3},
		{"LVIII", 58},
		{"MCMXCIV", 1994},
	}

	for _, tc := range testCases {
		actual := romanToInt(tc.input)
		if actual != tc.expected {
			t.Errorf("romanToInt(%s) = %d, expected %d", tc.input, actual, tc.expected)
		}
	}
}
