package main

import (
	"math"
	"testing"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var assigned bool
var prev int
var res int

func getMinimumDifference(root *TreeNode) int {
	res = math.MaxInt
	assigned = false
	dfs(root)
	return res
}

func dfs(node *TreeNode) {
	if node == nil {
		return
	}

	dfs(node.Left)

	if assigned {
		diff := node.Val - prev
		if diff < res {
			res = diff
		}
	}
	assigned = true
	prev = node.Val

	dfs(node.Right)
}

func TestGetMinimumDifference(t *testing.T) {
	testCases := []struct {
		root     *TreeNode
		expected int
	}{
		{
			root: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 1,
					},
					Right: &TreeNode{
						Val: 3,
					},
				},
				Right: &TreeNode{
					Val: 6,
				},
			},
			expected: 1,
		},
		{
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 0,
				},
				Right: &TreeNode{
					Val: 48,
					Left: &TreeNode{
						Val: 12,
					},
					Right: &TreeNode{
						Val: 49,
					},
				},
			},
			expected: 1,
		},
	}

	for _, tc := range testCases {
		actual := getMinimumDifference(tc.root)
		if actual != tc.expected {
			t.Errorf("getMinimumDifference() = %v, expected %v", actual, tc.expected)
		}
	}
}
