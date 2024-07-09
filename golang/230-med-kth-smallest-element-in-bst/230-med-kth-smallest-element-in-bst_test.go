package main

import (
	"testing"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	values := make([]int, 0)

	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}

		inorder(node.Left)
		values = append(values, node.Val)
		inorder(node.Right)
	}

	inorder(root)
	return values[k-1]
}

func TestKthSmallest(t *testing.T) {
	testCases := []struct {
		root     *TreeNode
		k        int
		expected int
	}{
		{
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 1,
					Right: &TreeNode{
						Val: 2,
					},
				},
				Right: &TreeNode{
					Val: 4,
				},
			},
			k:        1,
			expected: 1,
		},
		{
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val: 2,
						Left: &TreeNode{
							Val: 1,
						},
					},
					Right: &TreeNode{
						Val: 4,
					},
				},
				Right: &TreeNode{
					Val: 6,
				},
			},
			k:        3,
			expected: 3,
		},
	}

	for _, tc := range testCases {
		actual := kthSmallest(tc.root, tc.k)
		if actual != tc.expected {
			t.Errorf("kthSmallest() = %v, expected %v", actual, tc.expected)
		}
	}
}
