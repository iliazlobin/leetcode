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

func isValidBST(root *TreeNode) bool {
	var dfs func(node *TreeNode, left int, right int) bool
	dfs = func(node *TreeNode, left int, right int) bool {
		if node == nil {
			return true
		}
		if !(node.Val > left && node.Val < right) {
			return false
		}

		return dfs(node.Left, left, node.Val) && dfs(node.Right, node.Val, right)
	}

	return dfs(root, math.MinInt, math.MaxInt)
}

func TestIsValidBST(t *testing.T) {
	testCases := []struct {
		root     *TreeNode
		expected bool
	}{
		// {
		// 	root: &TreeNode{
		// 		Val: 2,
		// 		Left: &TreeNode{
		// 			Val: 1,
		// 		},
		// 		Right: &TreeNode{
		// 			Val: 3,
		// 		},
		// 	},
		// 	expected: true,
		// },
		// {
		// 	root: &TreeNode{
		// 		Val: 5,
		// 		Left: &TreeNode{
		// 			Val: 1,
		// 		},
		// 		Right: &TreeNode{
		// 			Val: 4,
		// 			Left: &TreeNode{
		// 				Val: 3,
		// 			},
		// 			Right: &TreeNode{
		// 				Val: 6,
		// 			},
		// 		},
		// 	},
		// 	expected: false,
		// },
		{
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 4,
				},
				Right: &TreeNode{
					Val: 6,
					Left: &TreeNode{
						Val: 3,
					},
					Right: &TreeNode{
						Val: 7,
					},
				},
			}, expected: false},
	}

	for _, tc := range testCases {
		actual := isValidBST(tc.root)
		if actual != tc.expected {
			t.Errorf("isValidBST() = %v, expected %v", actual, tc.expected)
		}
	}
}
