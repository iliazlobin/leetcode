package main

import (
	"reflect"
	"testing"
)

func asteroidCollision(asteroids []int) []int {
	res := []int{}

outer:
	for i := 0; i < len(asteroids); i += 1 {
		cur := asteroids[i]

		for len(res) > 0 {
			prev := res[len(res)-1]
			if prev > 0 && cur < 0 {
				if (-1 * cur) > prev {
					res = res[:len(res)-1]
					continue
				} else if (-1 * cur) < prev {
					continue outer
				} else {
					res = res[:len(res)-1]
					continue outer
				}
			}
			break
		}

		res = append(res, cur)
	}

	return res
}

func TestAsteroidCollision(t *testing.T) {
	testCases := []struct {
		asteroids []int
		expected  []int
	}{
		{[]int{5, 10, -5}, []int{5, 10}},
		{[]int{8, -8}, []int{}},
		{[]int{10, 2, -5}, []int{10}},
		{asteroids: []int{-2, -1, 1, 2}, expected: []int{-2, -1, 1, 2}},
		{asteroids: []int{-2, 1, -1, -2}, expected: []int{-2, -2}},
	}

	for _, tc := range testCases {
		actual := asteroidCollision(tc.asteroids)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("asteroidCollision(%v) = %v, expected %v", tc.asteroids, actual, tc.expected)
		}
	}
}
