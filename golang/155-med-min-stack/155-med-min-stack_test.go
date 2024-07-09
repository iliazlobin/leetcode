package main

import (
	"testing"
)

type MinStack struct {
	stack    []int
	minStack []int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	minVal := val
	if len(this.minStack) > 0 && this.minStack[len(this.minStack)-1] < minVal {
		minVal = this.minStack[len(this.minStack)-1]
	}
	this.minStack = append(this.minStack, minVal)
}

func (this *MinStack) Pop() {
	this.stack = this.stack[:len(this.stack)-1]
	this.minStack = this.minStack[:len(this.minStack)-1]
}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.minStack[len(this.minStack)-1]
}

func TestMinStack(t *testing.T) {
	minStack := Constructor()
	minStack.Push(-2)
	minStack.Push(0)
	minStack.Push(-3)
	if got := minStack.GetMin(); got != -3 {
		t.Errorf("MinStack.GetMin() = %d, want %d", got, -3)
	}
	minStack.Pop()
	if got := minStack.Top(); got != 0 {
		t.Errorf("MinStack.Top() = %d, want %d", got, 0)
	}
	if got := minStack.GetMin(); got != -2 {
		t.Errorf("MinStack.GetMin() = %d, want %d", got, -2)
	}
}

func TestMinStack_SequenceTwo(t *testing.T) {
	minStack := Constructor()
	minStack.Push(0)
	minStack.Push(1)
	minStack.Push(0)
	if got := minStack.GetMin(); got != 0 {
		t.Errorf("MinStack.GetMin() = %d, want %d", got, 0)
	}
	minStack.Pop()
	if got := minStack.GetMin(); got != 0 {
		t.Errorf("MinStack.GetMin() after pop = %d, want %d", got, 0)
	}
}
