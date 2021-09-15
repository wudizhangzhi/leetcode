package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

/*
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
*/
func maxSubArray(nums []int) int {
	result := nums[0]
	sum := 0
	for i := 0; i < len(nums); i++ {
		t := sum + nums[i]
		result = max(result, t)
		if t <= 0 {
			sum = 0
		} else {
			sum = t
		}
	}

	return result
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6)
	fmt.Println(maxSubArray([]int{5, 4, -1, 7, 8}) == 23)
	fmt.Println(maxSubArray([]int{1}) == 1)
}
