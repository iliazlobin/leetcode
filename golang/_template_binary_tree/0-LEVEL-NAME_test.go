package main

import (
	"testing"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getMinimumDifference(root *TreeNode) int {
	return 0
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
