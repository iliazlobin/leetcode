package main

import (
	"reflect"
	"testing"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	dummy := &ListNode{}
	dummy.Next = head

	pos := 0
	for ; pos < left-2 && head != nil; pos++ {
		head = head.Next
	}
	beforeStart := head

	for ; pos < right-1 && head != nil; pos++ {
		head = head.Next
	}
	atEnd := head
	afterEnd := head.Next
	atEnd.Next = nil

	prev := afterEnd
	head = beforeStart.Next
	var prevHead *ListNode
	for head != nil {
		temp := head.Next
		head.Next = prev
		prev = head
		prevHead = head
		head = temp
	}

	beforeStart.Next = prevHead

	return dummy.Next
}

func TestReverseBetween(t *testing.T) {
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
		head     []int
		left     int
		right    int
		expected []int
	}{
		{[]int{1, 2, 3, 4, 5}, 2, 4, []int{1, 4, 3, 2, 5}},
		{[]int{5}, 1, 1, []int{5}},
	}

	for _, tc := range testCases {
		head := createLinkedList(tc.head)
		actualHead := reverseBetween(head, tc.left, tc.right)
		actual := linkedListToSlice(actualHead)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("reverseBetween(%v, %d, %d) = %v, expected %v", tc.head, tc.left, tc.right, actual, tc.expected)
		}
	}
}
