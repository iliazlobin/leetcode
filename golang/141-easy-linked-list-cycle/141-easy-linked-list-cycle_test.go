package main

import (
	"testing"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	slow := head
	fast := head

	for {
		if fast.Next == nil || fast.Next.Next == nil {
			return false
		}
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
}

func TestHasCycle(t *testing.T) {
	// Helper function to create a linked list with a cycle
	createLinkedList := func(vals []int, pos int) *ListNode {
		if len(vals) == 0 {
			return nil
		}
		head := &ListNode{Val: vals[0]}
		current := head
		var cycleNode *ListNode
		if pos == 0 {
			cycleNode = head
		}
		for i := 1; i < len(vals); i++ {
			current.Next = &ListNode{Val: vals[i]}
			current = current.Next
			if i == pos {
				cycleNode = current
			}
		}
		if cycleNode != nil {
			current.Next = cycleNode
		}
		return head
	}

	testCases := []struct {
		vals     []int
		pos      int
		expected bool
	}{
		{[]int{3, 2, 0, -4}, 1, true},
		{[]int{1, 2}, 0, true},
		{[]int{1}, -1, false},
	}

	for _, tc := range testCases {
		head := createLinkedList(tc.vals, tc.pos)
		actual := hasCycle(head)
		if actual != tc.expected {
			t.Errorf("TestHasCycle with input list %v and pos %d failed: expected %v, got %v", tc.vals, tc.pos, tc.expected, actual)
		}
	}
}
