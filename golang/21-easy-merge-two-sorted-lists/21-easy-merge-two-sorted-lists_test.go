package main

import (
	"testing"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := ListNode{
		Next: list1,
	}
	for list1 != nil || list2 != nil {
	}
}

func TestMergeTwoLists(t *testing.T) {
	// Helper function to create a linked list from a slice
	createLinkedList := func(vals []int) *ListNode {
		if len(vals) == 0 {
			return nil
		}
		head := &ListNode{Val: vals[0]}
		current := head
		for _, val := range vals[1:] {
			current.Next = &ListNode{Val: val}
			current = current.Next
		}
		return head
	}

	// Helper function to convert a linked list to a slice
	linkedListToSlice := func(head *ListNode) []int {
		var vals []int
		for current := head; current != nil; current = current.Next {
			vals = append(vals, current.Val)
		}
		return vals
	}

	testCases := []struct {
		list1    []int
		list2    []int
		expected []int
	}{
		{[]int{1, 2, 4}, []int{1, 3, 4}, []int{1, 1, 2, 3, 4, 4}},
		{[]int{}, []int{}, []int{}},
		{[]int{}, []int{0}, []int{0}},
	}

	for _, tc := range testCases {
		l1 := createLinkedList(tc.list1)
		l2 := createLinkedList(tc.list2)
		mergedListHead := mergeTwoLists(l1, l2)
		actual := linkedListToSlice(mergedListHead)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("mergeTwoLists(%v, %v) = %v, expected %v", tc.list1, tc.list2, actual, tc.expected)
		}
	}
}
