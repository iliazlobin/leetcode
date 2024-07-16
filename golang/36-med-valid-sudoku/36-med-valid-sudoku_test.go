package main

import (
	"testing"
)

func isValidSudoku(board [][]byte) bool {
	colsSets := make([]map[byte]bool, 9)
	rowsSets := make([]map[byte]bool, 9)
	gridSets := make([]map[byte]bool, 9)

	for i := 0; i < 9; i += 1 {
		colsSets[i] = make(map[byte]bool)
		rowsSets[i] = make(map[byte]bool)
		gridSets[i] = make(map[byte]bool)
	}

	for r := 0; r < 9; r += 1 {
		for c := 0; c < 9; c += 1 {
			if board[r][c] == '.' {
				continue
			}

			if _, ok := colsSets[c][board[r][c]]; ok {
				return false
			}
			colsSets[c][board[r][c]] = true

			if _, ok := rowsSets[r][board[r][c]]; ok {
				return false
			}
			rowsSets[r][board[r][c]] = true

			gridInd := int(c/3) + int(r/3)*3
			if _, ok := gridSets[gridInd][board[r][c]]; ok {
				return false
			}
			gridSets[gridInd][board[r][c]] = true
		}
	}

	return true
}

func TestIsValidSudoku(t *testing.T) {
	testCases := []struct {
		board    [][]byte
		expected bool
	}{
		{
			board: [][]byte{
				{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
				{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
				{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
				{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
				{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
				{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
				{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
				{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
				{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
			},
			expected: true,
		},
		{
			board: [][]byte{
				{'8', '3', '.', '.', '7', '.', '.', '.', '.'},
				{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
				{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
				{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
				{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
				{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
				{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
				{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
				{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
			},
			expected: false,
		},
	}

	for _, tc := range testCases {
		actual := isValidSudoku(tc.board)
		if actual != tc.expected {
			t.Errorf("isValidSudoku(%v) = %v, expected %v", tc.board, actual, tc.expected)
		}
	}
}
