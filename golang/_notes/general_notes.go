package main

import (
	"strings"
	"testing"
	"unicode"
	"strconv"
	"sort"
	"math"
)

func climbStairs(n int) int {
	if n <= 3 {
		return n
	}
	first := 2
	second := 3
	res := 0
	for i := 4; i <= n; i++ {
		res = first + second
		first = second
		second = res
	}
	return res
}

func mySqrt(x int) int {
	if x < 2 {
		return x
	}

	left, right := 1, x
	for left <= right {
		mid := left + (right-left)/2
		square := mid * mid
		if square > x {
			right = mid - 1
		} else if square < x {
			left = mid + 1
		} else {
			return mid
		}
	}
	return right
}

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	return append([]int{1}, digits...)
}

func searchInsert(nums []int, target int) int {
	r := len(nums) - 1
	l := 0

	for l <= r {
		mid := int((r + l) / 2)
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return l
}

func letterCombinations(digits string) []string {
	res := []string{}
	var dfs func(i int, cur string)
	dfs = func(i int, cur string) {
		if i == len(digits) {
			if len(cur) > 0 {
				res = append(res, cur)
			}
			return
		}
		digit := digits[i:i+1]
		for _, c := range letters[digit] {
			dfs(i+1, cur+c)
		}
	}
	dfs(0, "")
	return res
}

func countNodes(root *TreeNode) int {
	cur = root.left
	for cur != nil {
		cur = cur.left
		leftDepth += 1
	}
	exponent := 3.0
	if leftDepth == rightDepth {
		return math.Pow(2, leftDepth) - 1
	}
	return 1 + countNodes(root.left) + countNodes(root.right)
}

func longestConsecutive(nums []int) int {
	sort.Ints(nums)
}

func isHappy(n int) bool {
	hMap := make(map[int]int)
	for _, c := range strconv.Itoa(cur) {
		new += int(c-'0') * int(c-'0')
}

func isPalindrome(s string) bool {
	lc := unicode.ToLower(rune(s[l]))
	if !(unicode.IsLetter(lc) || unicode.IsNumber(lc)) {
		continue
	}
}

func lengthOfLastWord(s string) int {
	parts := strings.Split(s, ",")
	fields := strings.Fields(s)
	idx := strings.Index(s, "substr")
	idx := strings.IndexRune(s, rune(s[2]))
	return len(list[len(list)-1])
}

// nums = [1,1,2]
func removeDuplicates(nums []int) int {
	l := 1
	for r := 1; r < len(nums); r++ {
		if nums[r] == nums[r-1] {
			continue
		}
		nums[l] = nums[r]
		l++
	}
	return l
}

func TestIsPalindrome(t *testing.T) {
	testCases := []struct {
		input    int
		expected bool
	}{
		{121, true},
		{-121, false},
		{10, false},
	}

	for _, tc := range testCases {
		actual := isPalindrome(tc.input)
		if actual != tc.expected {
			t.Errorf("isPalindrome(%d) = %v, expected %v", tc.input, actual, tc.expected)
		}
	}
}
