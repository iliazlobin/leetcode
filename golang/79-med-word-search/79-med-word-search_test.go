package main

import (
	"testing"
)

func exist(board [][]byte, word string) bool {
	rows := len(board)
	cols := len(board[0])
	visit := make(map[int]map[int]bool)
	for r := range board {
		visit[r] = make(map[int]bool)
	}

	var dfs func(r int, c int, w int) bool

	dfs = func(r int, c int, w int) bool {
		if r < 0 || r >= rows || c < 0 || c >= cols {
			return false
		}
		if board[r][c] != word[w] {
			return false
		}
		visited := visit[r][c]
		if visited {
			return false
		}

		if w == len(word)-1 {
			return true
		}
		visit[r][c] = true

		if dfs(r-1, c, w+1) || dfs(r, c-1, w+1) || dfs(r+1, c, w+1) || dfs(r, c+1, w+1) {
			return true
		}
		visit[r][c] = false
		return false
	}

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if dfs(r, c, 0) {
				return true
			}
		}
	}
	return false
}

func TestExist(t *testing.T) {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	testCases := []struct {
		word     string
		expected bool
	}{
		{"ABCCED", true},
		{"SEE", true},
		{"ABCB", false},
	}

	for _, tc := range testCases {
		actual := exist(board, tc.word)
		if actual != tc.expected {
			t.Errorf("exist(_, %s) = %v, expected %v", tc.word, actual, tc.expected)
		}
	}
}

func TestExistAAB(t *testing.T) {
	board := [][]byte{
		{'C', 'A', 'A'},
		{'A', 'A', 'A'},
		{'B', 'C', 'D'},
	}
	word := "AAB"
	expected := true
	actual := exist(board, word)
	if actual != expected {
		t.Errorf("TestExistAAB failed: expected %v, got %v", expected, actual)
	}
}
